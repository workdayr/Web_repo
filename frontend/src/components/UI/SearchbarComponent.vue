<script setup>
import {defineProps} from 'vue';
defineProps({
    text:String
});
</script>

<template>
    <div class="searchbar-container">
    <img class="search-icon" src="@/assets/Common/SearchIcon.svg" alt="Search Icon">
    <input class="searchbar" type="search" :placeholder="text" aria-label="Search">
  </div>
</template>

<style scoped>
@import "@/assets/styles/Dashboard/SearchbarComponent.css";
</style>