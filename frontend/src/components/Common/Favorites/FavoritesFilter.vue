<template>
    <div class="filter-menu">
        <div class="filter-menu__container">
            <div class="filter-group" >
                <label class="filter-menu-title">
                    <input type="checkbox" id="price-drop-only" v-model="filters.priceDropOnly"> Price Drop Only
                </label>
            </div>

            <div class="filter-group">
                <label class="filter-menu-title">Notification Status</label>
                <div class="nofification-options">
                    <label>
                        <input type="checkbox" id="notification-all" :checked="isNotificationAll"
                            @change="toggleAllNotifications"> <span class="check-all-indicator"></span> All
                    </label>
                    <label class="nested-option">
                        <input type="checkbox" name="notification-status" value="on" id="notification-on"
                            v-model="filters.notificationStatus"> On
                    </label>
                    <label class="nested-option">
                        <input type="checkbox" name="notification-status" value="off" id="notification-off"
                            v-model="filters.notificationStatus"> Off
                    </label>
                </div>
            </div>

            <div class="filter-group">
                <label class="filter-menu-title" for="sort-by">Sort By:</label>
                <select id="price-drop-sort" v-model="filters.sortBy">
                    <option value="liked_at-asc">Last Followed</option>
                    <option value="liked_at-desc">First Followed</option>
                    <option value="dropPrice-asc">Highest Drop Price</option>
                    <option value="dropPrice-desc">Lowest Drop Price</option>
                </select>
            </div>
        </div>
    </div>
</template>

<script setup>
import { computed, watch, reactive } from 'vue';
import { useFavoritesStore } from '@/store/useFavoritesStore';

const favoritesStore = useFavoritesStore();
const filters = reactive(favoritesStore.filters);

const isNotificationAll = computed(() => {
    return (filters.notificationStatus || []).length === 2;
});

const toggleAllNotifications = (event) => {
    if (event.target.checked) {
        filters.notificationStatus = ['on', 'off'];
    } else {
        filters.notificationStatus = [];
    }
};

watch(
    filters, // Watch the entire filters object
    () => {

        favoritesStore.applyFilters();
    },
    { deep: true }
);



</script>

<style scoped>
@import "@/assets/styles/Common/Favorites/FavoritesFilter.css";
</style>