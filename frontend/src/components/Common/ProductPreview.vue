<script setup>
import { defineProps } from 'vue';
import AddFavoriteButton from '@/components/Common/AddFavoriteButton.vue';
import { useFavoritesStore } from '@/store/useFavoritesStore';
const props = defineProps({
	product: {
		type: Object,
		required: true,
		validator: (product) => {
			// Validación más completa
			return 'product_id' in product && 'name' in product;
		}
	}
});

const favoritesStore = useFavoritesStore();

const handleFollowChange = (isFavorited) => {
	if (isFavorited) {
		favoritesStore.addFavorite(props.product.product_id);
	} else {
		favoritesStore.removeFavoriteByProductId(props.product.product_id);
	}
};

const handleImageError = (event) => {
	event.target.src = require('@/assets/Common/DefaultImage.svg');
};
</script>

<template>
	<div @click="product && product.product_id ? $router.push('/product/' + product.product_id) : console.warn('Product ID is missing or invalid')"
		class="product-preview">
		<img :src="product.primary_image_URL || require('@/assets/Common/DefaultImage.svg')"
			class="product-preview__image" loading="lazy" :alt="`Imagen de ${product.name}`"
			@error="handleImageError" />
		<div v-if="product.last_price_change_percentage && product.last_price_change_percentage< 1" class="product-preview__discount">
			<div class="product-preview__discount__card">
				<span class="product-preview__discount__title">{{ product.last_price_change_percentage.toFixed(2)}}%</span>
			</div>
			<span class="product-preview__discount__title">From {{ product.store_name}}</span>
		</div>
		<div class="product-preview__bottom">
			<div class="product-preview__data">
				<h2 class="product-preview__title">{{ product.name }}</h2>
				<div v-if="product.current_lowest_price" class="product-preview__price">
					<span class="price-symbol">{{ product.current_lowest_price.symbol || '$' }}</span>
					<span class="price-whole">
						{{ parseInt(product.current_lowest_price.price).toLocaleString({
							minimumFractionDigits: 0,
							maximumFractionDigits: 0
						}) }}
					</span>
					<span class="price-fraction">
						{{ (product.current_lowest_price.price % 1).toFixed(2).slice(2) }}
					</span>
				</div>
				<div v-else class="product-preview__price">Price not available</div>
			</div>

			<AddFavoriteButton :isFollowed="favoritesStore.isProductFollowed(product.product_id)"
				class="product-preview__favorite-button" @update:isFollowed="handleFollowChange"
				aria-label="Add to favorites" @click.stop />
		</div>
	</div>
</template>

<style scoped>
/* Tus estilos actuales se mantienen igual */
@import "@/assets/styles/Common/ProductPreview.css";
</style>