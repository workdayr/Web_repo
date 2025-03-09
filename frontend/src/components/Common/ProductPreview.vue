<script setup>
    import {defineProps} from 'vue';
    import AddFavoriteButton from '@/components/Common/AddFavoriteButton.vue';
    defineProps({
        symbol: {
            type: String,
            required: true,
        },
        priceWhole: {
            type: Number,
            required: true,
        },
        priceFraction: {
            type: Number,
            required: true,
        },
        title: {
            type: String,
            required: true,
        },
});
</script>
<template>
    <div class="product-preview">
        <img class="product-preview__image" alt="Product Image"/>
        <div class="product-preview__bottom">
            <div class="product-preview__data">
                <div class="product-preview__price">
                    <span class="price-symbol">{{symbol}}</span>
                    <span class="price-whole">{{priceWhole}}</span>
                    <span class="price-fraction">{{priceFraction}}</span>
                </div>
                <h2 class="product-preview__title">{{title}}</h2>
            </div>
            <AddFavoriteButton class="product-preview__favorite-button"/>
        </div>
    </div>
</template>
<style scoped>
@import "@/assets/styles/Common/ProductPreview.css";
</style>