<template>
    <div class="favorites-element">
        <input type="checkbox" name="favorite-selected" value="off">
        <img class="favorites-element__img" :src="imageSource" @error="useDefaultImage">
        <span class="favorites-element__title">{{ product.name }}</span>
        <PriceDropComponent :product="product" />
        <button class="favorites-element__button" @click="handleRemove">
            <img class="favorites-element__delete" src="@/assets/Common/delete.svg" alt="">
        </button>
    </div>
</template>

<script setup>
import { defineProps, ref, watch, defineEmits} from 'vue';
import PriceDropComponent from './PriceDropComponent.vue';

const props = defineProps({
    product: {
        type: Object,
        required: true,
    },
});

console.log(props.product);

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
  emit('remove-favorite', props.product.user_favorites_id);
};
</script>

<style scoped>
@import "@/assets/styles/Common/Favorites/FavoritesList.css";
</style>