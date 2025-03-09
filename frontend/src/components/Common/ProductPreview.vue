<script setup>
    import {defineProps} from 'vue';
    import AddFavoriteButton from '@/components/Common/AddFavoriteButton.vue';

    defineProps({
        product: {
        type: Object,
        required: true
    }
    });

</script>
<template>
    <div class="product-preview">
        <img :src="product.imageUrl || require('@/assets/Common/DefaultImage.svg')" class="product-preview__image" loading="lazy" alt="Product Image"/>
        
        <div class="product-preview__bottom">
            <div class="product-preview__data">
                <div class="product-preview__price">
                    <span class="price-symbol">{{product.symbol}}</span>
                    <span class="price-whole">{{Number(product.priceWhole).toLocaleString()}}</span>
                    <span class="price-fraction">{{product.priceFraction}}</span>
                </div>
                <h2 class="product-preview__title">{{product.title}}</h2>
            </div>
            <AddFavoriteButton class="product-preview__favorite-button"/>
        </div>
    </div>
</template>
<style scoped>
@import "@/assets/styles/Common/ProductPreview.css";
</style>