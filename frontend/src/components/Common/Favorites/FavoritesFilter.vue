<template>
    <div class="filter-menu">
        <div class="filter-menu__container">
            <div class="filter-group">
                <label>

                    <input type="checkbox" id="price-drop-only"> Price Drop Only
                </label>
            </div>

            <div class="filter-group">
                <label>Notification Status</label>
                <label>
                    <input type="checkbox" id="notification-all"> <span class="check-all-indicator"></span> All
                </label>
                <label class="nested-option">
                    <input type="checkbox" name="notification-status" value="on" id="notification-on"> Enabled
                </label>
                <label class="nested-option">
                    <input type="checkbox" name="notification-status" value="off" id="notification-off"> Disabled
                </label>
            </div>

            <div class="filter-group">
                <label for="price-drop-sort">Price Drop:</label>
                <select id="price-drop-sort">
                    <option value="">-- Select --</option>
                    <option value="low-to-high">Low to High</option>
                    <option value="high-to-low">High to Low</option>
                </select>
            </div>

            <div class="filter-group">
                <label for="date-followed-sort">Date Followed:</label>
                <select id="date-followed-sort">
                    <option value="newest-first">Newest First</option>
                    <option value="oldest-first">Oldest First</option>
                </select>
            </div>
        </div>
    </div>

</template>

<script setup>

</script>
<style scoped>
@import "@/assets/styles/Common/Favorites/FavoritesFilter.css";
</style>