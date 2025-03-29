import { defineStore } from 'pinia';
import { ref, computed, watch } from 'vue';
import { favoritesService } from '@/api/favoritesService'
import { useAuthStore } from './useAuthStore';
import { useRouter } from 'vue-router';


export const useFavoritesStore = defineStore('favoritesStore', () => {
    const favorites = ref([]);
    const loading = ref(false);
    const error = ref(null);
    const previous = ref(null);
    const next = ref(null);
    const hasMore = ref(true);
    const isDescendant = ref(true);
    const dataOrder = ref('dateFollowed');
    const dataHasBeenFetched = ref(false);
    const filters = ref({
        priceDropOnly: false,
        notificationStatus: [], // Will hold 'on' and/or 'off'
        sortBy: 'date-followed-asc'
    });
    const followedProducts = ref(new Set());
    const authStore = useAuthStore();
    const router = useRouter();

    const checkAuthorization = () => {
        
        if (!authStore.isAuthenticated) {
            router.push('/login');
            return false;
        } else {
            return true
        }
    }

    const fetchFavorites = async () => {
        if (!hasMore.value || loading.value || dataHasBeenFetched.value || !checkAuthorization()) return;
        loading.value = true;
        error.value = null;

        try {
            const response = await favoritesService.getFavorites(
                {

                    pageSize: 10,
                    sortBy: dataOrder.value,
                    desc: isDescendant.value
                }
            );
            previous.value = response.data.previous;
            next.value = response.data.next;
            hasMore.value = next.value != null;
            favorites.value.push(...response.data.results);
            response.data.results.forEach(favorite => {
                followedProducts.value.add(favorite.product_id);
            });
            dataHasBeenFetched.value = true;
        } catch (err) {
            console.error("fetch error:", err);
            error.value = 'Failed to load favorites';
        } finally {
            loading.value = false;
        }
    };

    const applyFilters = () => {
        if (!checkAuthorization()) return;
        const hasNotificationFilter = filters.value.notificationStatus.length === 1;
        const shouldShowActiveNotifications = hasNotificationFilter
            ? filters.value.notificationStatus[0] === 'on'
            : null;

        favorites.value = favorites.value.filter(favorite => {
            const hasPriceDrop = !filters.value.priceDropOnly || favorite.product.priceDrop > 0;

            const matchesNotificationFilter = shouldShowActiveNotifications !== null
                ? shouldShowActiveNotifications
                    ? favorite.activeNotifications
                    : !favorite.activeNotifications
                : true;

            return hasPriceDrop && matchesNotificationFilter;
        });
        const [field, order] = filters.value.sortBy.split('-');
        isDescendant.value = order == 'desc';
        dataOrder.value = field;

    };

    const addFavorite = async (product_id) => {
        if (!checkAuthorization()) return;
        if (followedProducts.value.has(product_id)) return;
        try {
            await favoritesService.addFavorites(product_id);
            followedProducts.value.add(product_id); // Add to followedProducts on add
            dataHasBeenFetched.value = false;
            hasMore.value = true;
        } catch (error) {
            console.error('Failed to add favorite:', error);
        }
    };

    const removeFavorite = async (favorite_id) => {
        if (!checkAuthorization()) return;
        try {
            await favoritesService.removeFavorites(favorite_id);
            const index = favorites.value.findIndex(fav => fav.user_favorites_id === favorite_id);
            if (index !== -1) {
                const productIdToRemove = favorites.value[index].product_id;
                followedProducts.value.delete(productIdToRemove);
                favorites.value.splice(index, 1);
            }
        } catch (err) {
            console.log(err);
            return false;
        }
    };

    const removeFavoriteByProductId = async (productId) => {
        if (!checkAuthorization()) return;
        const favoriteToRemove = favorites.value.find(fav => fav.product_id === productId);
        if (favoriteToRemove) {
            removeFavorite(favoriteToRemove.user_favorites_id);
        } else {
            console.log(`Product with ID ${productId} not found in favorites.`);
        }
    };

    const toggleNotifications = async (isActive, favorite_id) => {
        if (!checkAuthorization()) return;
        favoritesService.patchFavorites(favorite_id, { "active_notifications": isActive });
        const index = favorites.value.findIndex(fav => fav.user_favorites_id === favorite_id);
        if (index !== -1) favorites[index].active_notifications = isActive;
    };

    const changePriceTreshold = async (priceTreshold, favorite_id) => {
        if (!checkAuthorization()) return;
        favoritesService.patchFavorites(favorite_id, { "price_threshold": priceTreshold });
        const index = favorites.value.findIndex(fav => fav.user_favorites_id === favorite_id);
        if (index !== -1) favorites[index].price_threshold = priceTreshold;
    };


    const changePercentageTreshold = async (percentageTreshold, favorite_id) => {
        if (!checkAuthorization()) return;
        favoritesService.patchFavorites(favorite_id, { "percentage_threshold": percentageTreshold });
        const index = favorites.value.findIndex(fav => fav.user_favorites_id === favorite_id);
        if (index !== -1) favorites[index].percentage_threshold = percentageTreshold;
    };

    const isProductFollowed = computed(() => {
        return (productId) => {
            return followedProducts.value.has(productId);
        };
    });


    watch(
        () => authStore.isAuthenticated,
        (isAuthenticated) => {
            if (isAuthenticated && !dataHasBeenFetched.value) {
                fetchFavorites();
            }
        },
        { immediate: true } // This will also run the callback on component mount
    );


    return {
        favorites,
        loading,
        error,
        filters,
        dataHasBeenFetched,
        fetchFavorites,
        applyFilters,
        addFavorite,
        removeFavorite,
        removeFavoriteByProductId,
        toggleNotifications,
        changePriceTreshold,
        changePercentageTreshold,
        isProductFollowed,

    };
});
