<template>
  <section id="Homepage">
    <NavbarComponent :is-always-compact="false"/>

    <CarouselComponent :slides="carouselSlides"/>

    <div class="hompage-content">
      <FindBestPrices/>
      
      <HomepageSection 
        v-for="section in visibleSections"
        class="homepage-section" 
        :key="section.id" 
        :title="section.title" 
        :icon="section.icon" 
        :products="section.products"
      />
    </div>

    <FooterComponent/>
  </section>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import axios from 'axios';
import NavbarComponent from '@/components/Layout/NavbarComponent.vue';
import CarouselComponent from '@/components/Layout/CarouselComponent.vue'; 
import FindBestPrices from '@/components/Homepage/FindBestPrices.vue';
import HomepageSection from '@/components/Homepage/HomepageSection.vue';
import FooterComponent from '@/components/Layout/FooterComponent.vue';

const carouselSlides = ref([
  {
    "text": "Compare prices across \ndifferent websites",
    "gradient": "linear-gradient(to bottom, #4D1270, #561960)",
    "icon": require("@/assets/Carrusel_icons/Slide1.svg"),
    "textPosition": "center-left",
    "iconPosition": "center-right"
  }
]);

const sectionsData = ref([
  {
    id: 0, 
    title: "Best Sales", 
    icon: require("@/assets/Layout/Footer/instagram-icon.png"),
    products: []
  },
  {
    id: 1, 
    title: "You may also like", 
    products: []
  }
]);

const visibleSections = computed(() => {
  return sectionsData.value.filter(section => section.products.length > 0);
});

onMounted(async () => {
  try {
    const response = await axios.get('http://127.0.0.1:8000/api/products/');
    const allProducts = response.data || [];
    
    const half = Math.ceil(allProducts.length / 2);
    sectionsData.value = [
      { ...sectionsData.value[0], products: allProducts.slice(0, half) },
      { ...sectionsData.value[1], products: allProducts.slice(half) }
    ];
  } catch (error) {
    console.error("Error al obtener productos:", error);
  }
});
</script>

<style scoped>
@import "@/assets/styles/Views/HomepageView.css";
</style>