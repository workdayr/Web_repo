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

// Debug detallado
console.log('Datos del producto:', {
  id: props.product.product_id,
  name: props.product.name,
  image: props.product.imageUrl,
  price: props.product.lowest_price,
  currency: props.product.symbol
});

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
  <div  class="product-preview">
    <img @click="$router.push('/product')"
      :src="product.imageUrl || require('@/assets/Common/DefaultImage.svg')" 
      class="product-preview__image"
      loading="lazy" 
      :alt="`Imagen de ${product.name}`"
      @error="handleImageError"
    />

    <div class="product-preview__bottom">
      <div @click="$router.push('/product')" class="product-preview__data">
        <h2 class="product-preview__title">{{ product.name }}</h2>

        <!-- Precio completo formateado -->
        <div v-if="product.lowest_price" class="product-preview__price">
          <span class="price-symbol">{{ product.symbol || '$' }}</span>
          <span class="price-whole">
            {{ parseInt(product.lowest_price).toLocaleString() }}
          </span>
          <span class="price-fraction">
            {{ (product.lowest_price % 1).toFixed(2).slice(2) || '00' }}
          </span>
        </div>
        <div v-else class="product-preview__price">Precio no disponible</div>
      </div>

      <AddFavoriteButton 
        :isFollowed="favoritesStore.isProductFollowed(product.product_id)"
        class="product-preview__favorite-button" 
        @update:isFollowed="handleFollowChange"
        aria-label="Añadir a favoritos"
        @click.stop
      />
    </div>
  </div>
</template>

<style scoped>
/* Tus estilos actuales se mantienen igual */
@import "@/assets/styles/Common/ProductPreview.css";
</style>