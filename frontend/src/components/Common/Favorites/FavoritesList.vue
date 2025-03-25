<template>
    <div class="favorites-element">
        <input type="checkbox" name="favorite-selected" value="off">
        <img class="favorites-element__img" :src="product.imageUrl || require('@/assets/Common/DefaultImage.svg')">
        <span class="favorites-element__title">{{ product.title }}</span>
        <PriceDropComponent :product="product"/>
        <button class="favorites-element__button">
            <img class="favorites-element__delete" src="@/assets/Common/delete.svg" alt="">
        </button>
    </div>

</template>

<script setup>
import {defineProps} from 'vue'
import PriceDropComponent from './PriceDropComponent.vue';
defineProps({
    product: {
        type: Object,
        required: true
    }
});
</script>
<style scoped>
@import "@/assets/styles/Common/Favorites/FavoritesList.css";
</style>