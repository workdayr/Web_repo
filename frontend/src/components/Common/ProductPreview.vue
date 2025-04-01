<script setup>
import { defineProps} from 'vue';
import AddFavoriteButton from '@/components/Common/AddFavoriteButton.vue';
import { useFavoritesStore } from '@/store/useFavoritesStore';
const props = defineProps({
    product: {
        type: Object,
        required: true
    }
});


const favoritesStore = useFavoritesStore();

const handleFollowChange = (newValue) => {
    if(newValue){
        favoritesStore.addFavorite(props.product.product_id);
    }else{
        favoritesStore.removeFavoriteByProductId(props.product.product_id);
    }
};


</script>
<template>
    <div class="product-preview">
        <img :src="product.imageUrl || require('@/assets/Common/DefaultImage.svg')" class="product-preview__image"
            loading="lazy" alt="Product Image" />

        <div class="product-preview__bottom">
            <div class="product-preview__data">
                <div class="product-preview__price">
                    <span class="price-symbol">{{ product.symbol }}</span>
                    <span class="price-whole">{{ Number(product.priceWhole).toLocaleString() }}</span>
                    <span class="price-fraction">{{ product.priceFraction }}</span>
                </div>
                <h2 class="product-preview__title">{{ product.title }}</h2>
            </div>
            <AddFavoriteButton :isFollowed="favoritesStore.isProductFollowed(props.product.product_id)" class="product-preview__favorite-button"
                @update:isFollowed="handleFollowChange" />
        </div>
    </div>
</template>
<style scoped>
@import "@/assets/styles/Common/ProductPreview.css";
</style>