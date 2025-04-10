import { defineStore } from 'pinia';
import { ref, computed, watch } from 'vue';
import { favoritesService } from '@/api/favoritesService'
import { useAuthStore } from './useAuthStore';


export const useFavoritesStore = defineStore('favoritesStore', () => {
    const favorites = ref([]);
    const dataHasBeenFetched = ref(false);
    const loading = ref(false);
    const message = ref(null);
    const previous = ref(null);
    const next = ref(null);
    const hasMore = ref(true);
    const followedProducts = ref(new Map());
    const productFollowStatus = ref(new Set());
    const pendingOperations = ref(new Set());
    const authStore = useAuthStore(); 
    const {checkAuthorization } = authStore;
    const filteredFavoriteIndexes = ref([]);
    
    // Filter variables
    const isDescendant = ref(false);
    const dataOrder = ref('liked_at');
    const filters = ref({
        priceDropOnly: false,
        notificationStatus: [], // Will hold 'on' and/or 'off'
        sortBy: 'liked_at-asc'
    });

    const fetchFavorites = async () => {
        if (!hasMore.value || loading.value || dataHasBeenFetched.value || !checkAuthorization()) return;
        loading.value = true;
        message.value = null;
        try {
            const response = await favoritesService.getFavorites({
                pageSize: 10,
                sortBy: dataOrder.value,
                desc: isDescendant.value
            });

            previous.value = response.data.previous;
            next.value = response.data.next;
            hasMore.value = !!next.value;

            favorites.value = response.data.results;
            followedProducts.value.clear(); 

            favorites.value.forEach((fav, idx) => {
                followedProducts.value.set(fav.product_id, idx);
                productFollowStatus.value.add(fav.product_id);
            });

            dataHasBeenFetched.value = true;
            applyFilters();
        } catch (err) {
            console.error('Fetch error:', err);
            message.value = 'Failed to load favorites';
        } finally {
            loading.value = false;
        }
    };

    const applyFilters = () => {
        if (!checkAuthorization()) return;
    
        filteredFavoriteIndexes.value = favorites.value
            .map((favorite, index) => ({ favorite, index }))
            .filter(({ favorite }) => {
                const hasPriceDrop = !filters.value.priceDropOnly || favorite.product.last_price_change_percentage < 0;
                const hasNotificationFilter = filters.value.notificationStatus.length === 1;
                const shouldShowActiveNotifications = hasNotificationFilter
                    ? filters.value.notificationStatus[0] === 'on'
                    : null;
                const matchesNotificationFilter = shouldShowActiveNotifications !== null
                    ? shouldShowActiveNotifications
                        ? favorite.active_notifications
                        : !favorite.active_notifications
                    : true;
    
                return hasPriceDrop && matchesNotificationFilter;
            })
            .map(({ index }) => index); 
    };

    watch(() => filters.value.sortBy, (newVal, oldVal) => {
        if (newVal !== oldVal) {
            const [field, order] = filters.value.sortBy.split('-');
            dataOrder.value = field;
            isDescendant.value = order=='desc';
            dataHasBeenFetched.value = false;
            hasMore.value=true;
            fetchFavorites();
        }
    });

    const addFavorite = async (product_id) => {
        if (!checkAuthorization() || isProductFollowed.value(product_id) || pendingOperations.value.has(product_id)) return;
        pendingOperations.value.add(product_id);
        try {
            await favoritesService.addFavorites(product_id);
            followedProducts.value.set(product_id, favorites.value.length); // Store index
            productFollowStatus.value.add(product_id);
            dataHasBeenFetched.value = false;
            hasMore.value = true;
        } catch (error) {
            console.error('Failed to add favorite:', error);
        } finally {
            pendingOperations.value.delete(product_id);
        }
    };

    const removeFavoriteByProductId = async (product_id) => {
        if (!checkAuthorization() || pendingOperations.value.has(product_id)) return;
        pendingOperations.value.add(product_id);

        if (isProductFollowed.value(product_id)) {
            const index = followedProducts.value.get(product_id);
            favorites.value.splice(index, 1);
            followedProducts.value.delete(product_id);
            productFollowStatus.value.delete(product_id);
            applyFilters();
        }

        try {
            await favoritesService.removeFavoritesByProductId(product_id);
        } catch (err) {
            console.error('Failed to remove favorite:', err);
        } finally {
            pendingOperations.value.delete(product_id);
        }
    };

    const removeFavorite = async (favorite_id) => {
        if (!checkAuthorization()) return;

        const index = favorites.value.findIndex(fav => fav.user_favorites_id === favorite_id);
        if (index === -1) return;

        const productIdToRemove = favorites.value[index].product_id;
        if (pendingOperations.value.has(productIdToRemove)) return;

        pendingOperations.value.add(productIdToRemove);
        try {
            await favoritesService.removeFavorites(favorite_id);
            followedProducts.value.delete(productIdToRemove);
            productFollowStatus.value.delete(productIdToRemove);
            favorites.value.splice(index, 1);
            applyFilters();
        } catch (err) {
            console.error('Failed to remove favorite:', err);
        } finally {
            pendingOperations.value.delete(productIdToRemove);
        }
    };

    const updateFavorite = async (product_id, data) => {
        if (!checkAuthorization() || pendingOperations.value.has(product_id)) return;
        const index = followedProducts.value.get(product_id);
        if (index === undefined) return;
        pendingOperations.value.add(product_id);

        try {
            await favoritesService.patchFavorites(favorites[index].user_favorites_id, data);
            Object.assign(favorites.value[index], data);
            applyFilters();
        } catch (err) {
            console.error("Failed to update favorite:", err);
        } finally {
            pendingOperations.value.delete(product_id);
        }
    };

    const toggleNotifications = async (product_id, isActive) => {
        await updateFavorite(product_id, { active_notifications: isActive });
    };

    const changePriceThreshold = async (product_id, priceThreshold) => {
        await updateFavorite(product_id, { price_threshold: priceThreshold });
    };

    const changePercentageThreshold = async (product_id, percentageThreshold) => {
        await updateFavorite(product_id, { percentage_threshold: percentageThreshold });
    };

    const isProductFollowed = computed(() => (product_id) => productFollowStatus.value.has(product_id));

    watch(
        () => authStore.isAuthenticated,
        (isAuthenticated) => {
            if (isAuthenticated && !dataHasBeenFetched.value) {
                fetchFavorites();
            }
        },
        { immediate: true }
    );

    return {
        favorites,
        filteredFavoriteIndexes,
        dataHasBeenFetched,
        followedProducts,
        isProductFollowed,
        pendingOperations,
        message,
        filters,
        fetchFavorites,
        addFavorite,
        applyFilters,
        removeFavorite,
        removeFavoriteByProductId,
        toggleNotifications,
        changePriceThreshold,
        changePercentageThreshold
    };
});