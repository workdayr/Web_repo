<template>
  <section id="Homepage">
    <NavbarComponent :is-always-compact="false"/>

    <CarouselComponent :slides="carouselSlides"/>

    <div class="hompage-content">
      <FindBestPrices/>
      
      <HomepageSection 
        v-for="section in sections"
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
import { ref, onMounted} from 'vue';
import {homepageService} from '@/api/homepageService.js';
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
  },
  {
    "text": "Compare prices across \ndifferent ",
    "gradient": "linear-gradient(to bottom, #4D1270, #561960)",
    "icon": require("@/assets/Carrusel_icons/Slide1.svg"),
    "textPosition": "center-left",
    "iconPosition": "center-right"
  }
]);

const sections = ref([]);

onMounted(async () => {
  try {
    const response = await homepageService.getSections();
    console.log('fetching sections');
    console.log(response.data);
    sections.value = response.data;
  } catch (error) {
    console.error("error trying to fetch products:", error);
  }
});
</script>

<style scoped>
@import "@/assets/styles/Views/HomepageView.css";
</style>