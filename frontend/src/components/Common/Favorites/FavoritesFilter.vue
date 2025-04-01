<template>
    <div class="filter-menu">
        <div class="filter-menu__container">
            <div class="filter-group">
                <label>
                    <input type="checkbox" id="price-drop-only" v-model="filters.priceDropOnly"> Price Drop Only
                </label>
            </div>

            <div class="filter-group">
                <label>Notification Status</label>
                <label>
                    <input type="checkbox" id="notification-all" :checked="isNotificationAll"
                        @change="toggleAllNotifications"> <span class="check-all-indicator"></span> All
                </label>
                <label class="nested-option">
                    <input type="checkbox" name="notification-status" value="on" id="notification-on"
                        v-model="filters.notificationStatus"> Enabled
                </label>
                <label class="nested-option">
                    <input type="checkbox" name="notification-status" value="off" id="notification-off"
                        v-model="filters.notificationStatus"> Disabled
                </label>
            </div>

            <div class="filter-group">
                <label for="sort-by">Sort By:</label>
                <select id="price-drop-sort" v-model="filters.sortBy">
                    <option value="liked_at-asc">Last Followed</option>
                    <option value="liked_at-desc">First Followed</option>
                    <option value="dropPrice-desc">Highest Drop Price</option>
                    <option value="dropPrice-asc">Lowest Drop Price</option>
                </select>
            </div>
        </div>
    </div>
</template>

<script setup>
import { computed, toRefs, watch } from 'vue';
import { useFavoritesStore } from '@/store/useFavoritesStore';

const favoritesStore = useFavoritesStore();

const { filters } = toRefs(favoritesStore);


const isNotificationAll = computed(() => {
    return (filters.value.notificationStatus || []).length === 2;
});


const toggleAllNotifications = (event) => {
    if (event.target.checked) {
        filters.notificationStatus = ['on', 'off'];
    } else {
        filters.notificationStatus = [];
    }
};

// Optional: Watch for changes in the filters object
watch(
    () => filters.value,
    () => {
        favoritesStore.applyFilters();
    },
    { deep: true }
);



</script>

<style scoped>
@import "@/assets/styles/Common/Favorites/FavoritesFilter.css";
</style>