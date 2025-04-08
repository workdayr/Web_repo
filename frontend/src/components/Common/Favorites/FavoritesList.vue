<template>
    <div class="favorites-element" v-if="product">
        <input type="checkbox" name="favorite-selected" value="off">
        <img class="favorites-element__img" :src="imageSource" @error="useDefaultImage">
        <span class="favorites-element__title">{{ product?.name }}</span>
        <PriceDropComponent :current-price="product?.current_lowest_price?.price"
            :price-drop="product?.last_price_change_percentage" :date="product?.current_lowest_price?.price"
            :store="product?.current_lowest_price?.price" />
        <button class="favorites-element__button" @click="handleRemove">
            <img class="favorites-element__delete" src="@/assets/Common/delete.svg" alt="">
        </button>
    </div>
</template>

<script setup>
import { defineProps, ref, watch, defineEmits } from 'vue';
import PriceDropComponent from './PriceDropComponent.vue';

const props = defineProps({
    product: {
        type: Object,
        required: true,
    },
});

const defaultImageURL = require('@/assets/Common/DefaultImage.svg');
const imageSource = ref(props.product?.primary_image_URL || defaultImageURL);

const useDefaultImage = () => {
    imageSource.value = defaultImageURL;
};

watch(() => props.product?.primary_image_URL, (newURL) => {
    imageSource.value = newURL || defaultImageURL;
});

const emit = defineEmits(['remove-favorite']);

const handleRemove = () => {
    // Assuming your product prop has a user_favorites_id
    emit('remove-favorite',1);
};
</script>

<style scoped>
@import "@/assets/styles/Common/Favorites/FavoritesList.css";
</style>