<template>
    <div v-if="hover" id="overlay"></div>
    <div class="favs" :class="{'favs_overlay': hover}" @mouseover="togglePopup(true)" @mouseleave="togglePopup(false)">
        <button class="favs__button" @click="addToFavorites">
            <svg class="favs__image" width="26" height="25" viewBox="0 0 26 25" xmlns="http://www.w3.org/2000/svg">
                <path
                    d="M14.2896 2.15019L17.0326 6.76796C17.3834 7.35859 17.9618 7.77882 18.6319 7.92996L23.8713 9.11168C24.9817 9.36212 25.4194 10.7095 24.6684 11.5647L21.1242 15.6004C20.6709 16.1166 20.45 16.7965 20.5133 17.4805L21.0085 22.8287C21.1134 23.9621 19.9673 24.7948 18.9218 24.3447L13.9885 22.2211C13.3575 21.9495 12.6425 21.9495 12.0115 22.2211L7.0782 24.3447C6.03271 24.7948 4.88657 23.9621 4.99151 22.8287L5.48669 17.4805C5.55002 16.7965 5.32909 16.1166 4.87579 15.6004L1.33164 11.5647C0.580552 10.7095 1.01834 9.36212 2.12868 9.11168L7.36806 7.92996C8.03819 7.77882 8.61659 7.35858 8.96742 6.76796L11.7104 2.15019C12.2916 1.17158 13.7084 1.17158 14.2896 2.15019Z"
                    stroke="white" />
            </svg>
        </button>
        <Transition name="popup">
            <div class="favs__popup" v-if="hover">
                <div class="favs__popup--header">
                    <h2 class="favs__popup--title">Favorites</h2>
                    <button class="favs__notis--button" @click="handleNotificationsChange">
                        <svg class="favs__popup--notis-icon" :class="{ activeNotis: activeNotis }" width="20"
                            height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path fill-rule="evenodd" clip-rule="evenodd"
                                d="M5.03976 0.418603C5.36337 0.869189 5.26042 1.49679 4.80984 1.82039C3.94365 2.44248 3.2379 3.26172 2.75088 4.21044C2.26385 5.15916 2.00953 6.21014 2.00893 7.27658C2.00862 7.83132 1.55865 8.28079 1.0039 8.28047C0.449146 8.28016 -0.000313798 7.83018 1.64384e-07 7.27544C0.00078471 5.89031 0.331105 4.52524 0.963677 3.29299C1.59624 2.06074 2.51292 0.996673 3.63797 0.188681C4.08855 -0.134923 4.71616 -0.0319837 5.03976 0.418603ZM5.11342 3.43939C6.24366 2.30915 7.7766 1.67418 9.375 1.67418C10.9734 1.67418 12.5063 2.30915 13.6366 3.43939C14.7668 4.56962 15.4018 6.10257 15.4018 7.70097V12.3885C15.4018 12.7437 15.5429 13.0843 15.7941 13.3355C16.0452 13.5866 16.3859 13.7278 16.7411 13.7278C17.1108 13.7278 17.4107 14.0276 17.4107 14.3974C17.4107 14.7672 17.1108 15.067 16.7411 15.067H2.00893C1.6391 15.067 1.33929 14.7672 1.33929 14.3974C1.33929 14.0276 1.6391 13.7278 2.00893 13.7278C2.36413 13.7278 2.70478 13.5866 2.95595 13.3355C3.20711 13.0843 3.34821 12.7437 3.34821 12.3885V7.70097C3.34821 6.10257 3.98318 4.56962 5.11342 3.43939ZM7.03125 17.7456C7.03125 17.1909 7.48097 16.7411 8.03571 16.7411H10.7143C11.269 16.7411 11.7188 17.1909 11.7188 17.7456C11.7188 18.3003 11.269 18.7501 10.7143 18.7501H8.03571C7.48097 18.7501 7.03125 18.3003 7.03125 17.7456ZM15.1121 0.188681C14.6614 -0.134923 14.0338 -0.0319837 13.7103 0.418603C13.3866 0.869189 13.4896 1.49679 13.9402 1.82039C14.8063 2.44248 15.5121 3.26172 15.9991 4.21044C16.4862 5.15916 16.7405 6.21014 16.7411 7.27658C16.7413 7.83132 17.1913 8.28079 17.7461 8.28047C18.3008 8.28016 18.7503 7.83018 18.75 7.27544C18.7492 5.89031 18.4189 4.52524 17.7864 3.29299C17.1537 2.06074 16.2371 0.996673 15.1121 0.188681Z"
                                stroke="#F5F5F5" stroke-width="1" transform="scale(0.9), translate(1, 1)" />
                        </svg>
                    </button>

                </div>
                <div class="favs__popup--content">
                    <div class="favs__popup--content-filters">
                        <button @mouseover="displayFilters=true" @mouseleave="displayFilters=false" class="favs__popup--content-filters-button">
                            <span class="favs__popup--content-filters-text"
                            >Filter By</span>
                            <FavoritesFilter v-if="displayFilters" />
                        </button>
                        <label class="favs__popup--content-filters-text">
                            Check all
                            <input type="checkbox" name="notification-status" value="off" id="notification-off">
                        </label>
                    </div>
                    <div class="favs__popup--content-list">
                        <FavoritesList v-for="index in favoritesStore.filteredFavoriteIndexes"
                            :key="favoritesStore.favorites[index].user_favorites_id"
                            :product="favoritesStore.favorites[index].product"
                            @remove-favorite="handleRemoveFavorite(favoritesStore.favorites[index].user_favorites_id, $event)" />
                    </div>
                </div>
            </div>
        </Transition>
    </div>
</template>
<script setup>
import { ref } from 'vue';
import FavoritesFilter from '@/components/Common/Favorites/FavoritesFilter.vue';
import FavoritesList from '@/components/Common/Favorites/FavoritesList.vue';
import { useFavoritesStore } from '@/store/useFavoritesStore';
const hover = ref(false);
const activeNotis = ref(false);
const displayFilters = ref(false);

const favoritesStore = useFavoritesStore();

const handleNotificationsChange = async () => {
    activeNotis.value = !activeNotis.value;
}

const togglePopup = async (isOpen) => {
    hover.value = isOpen;
    if (isOpen && !favoritesStore.dataHasBeenFetched) {
        await favoritesStore.fetchFavorites();
    }
}

const handleRemoveFavorite = (favoriteId) => {
    // Perform your logic here, e.g., remove the item from the store
    favoritesStore.removeFavorite(favoriteId);
};

</script>

<style scoped>
@import "@/assets/styles/Common/Favorites/FavoritesComponent.css";
</style>
