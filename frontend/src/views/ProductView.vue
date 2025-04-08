<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue';
import { useRoute } from 'vue-router';

import NavBarComponent from '@/components/Layout/NavbarComponent.vue';
import FooterComponent from '@/components/Layout/FooterComponent.vue';
import PriceCard from '@/components/UI/PriceCard.vue';
import AddFavoriteButton from '@/components/Common/AddFavoriteButton.vue';

const screenWidth = ref(window.innerWidth);
const isDescriptionExpanded = ref(false);
const productData = ref(null);
const loading = ref(true);
const error = ref(null);
const selectedImage = ref(null);
const thumbnails = ref([]);

const route = useRoute();
const productId = ref(route.params.productId); // Change the route if necessary

// Methods
const updateScreenWidth = () => {
  screenWidth.value = window.innerWidth;
};

const toggleDescription = () => {
  isDescriptionExpanded.value = !isDescriptionExpanded.value;
};

const changeImage = (newImage) => {
  selectedImage.value = newImage;
};

const fetchProductData = async () => {
  try {
    const response = await fetch(`/api/products?id=${productId.value}&extra_fields=primary_image_URL`);
    if (!response.ok) throw new Error('Error at loading data for this product');
    productData.value = await response.json();
  } catch (err) {
    error.value = err.message;
  } finally {
    loading.value = false;
  }
};

onMounted(() => {
  window.addEventListener('resize', updateScreenWidth);
  fetchProductData();
});

onBeforeUnmount(() => {
  window.removeEventListener('resize', updateScreenWidth);
});
</script>



<template>
  <div class="product-view">
    <NavBarComponent />

    <div class="first-half">
      <div v-if="screenWidth >= 766" class="product-section">

        <img :src="selectedImage" alt="Product Image" class="product-image">

        <div class="thumbnail-container">
          <img v-for="(thumb, index) in thumbnails" :key="index" :src="thumb" alt="Thumbnail" class="thumbnail-image"
            @click="changeImage(thumb)">
        </div>
      </div>
      <div class="product-details">
        <h2 class="product-title">{{ productData?.name || 'Loading name...' }}</h2>
        <div v-if="screenWidth < 766" class="product-section">

          <img :src="selectedImage" alt="Product Image" class="product-image">

          <div class="thumbnail-container">
            <img v-for="(thumb, index) in thumbnails" :key="index" :src="thumb" alt="Thumbnail" class="thumbnail-image"
              @click="changeImage(thumb)">
          </div>
        </div>
        <p class="price-label">Lowest price:</p>
        <p class="product-price">{{ productData?.price || 'Loading price...' }}</p>
        <p class="store-product">on {{ productData?.store || 'Loading store...' }}</p>

        <div class="description-container">
          <p class="description-text"
            :class="{ 'collapsed': !isDescriptionExpanded, 'expanded': isDescriptionExpanded }"
            @click="toggleDescription">
            {{ productData?.description || 'Loading description...' }}
          </p>
        </div>

        <div class="favorite-button-container">
          <AddFavoriteButton />
          <p class="follow-text">Follow product</p>
        </div>
      </div>
    </div>

    <div class="dynamic-table-section">
    </div>

    <div class="price-comparison">
      <PriceCard v-for="(offer, index) in productData?.prices || []" :key="index" :store="offer.store"
        :price="offer.price" :features="offer.features" />
    </div>


  </div>
  <FooterComponent />
</template>

<style scoped>
@import "@/assets/styles/Product/ProductView.css";
</style>