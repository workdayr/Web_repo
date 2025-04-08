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
      <div ref="scrollSentinel"></div>
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
const sectionIndex = ref(0);
const hasMoreSections = ref(true);
const isLoading = ref(false);
const scrollSentinel = ref(null);

onMounted(async () => {
  const observer = new IntersectionObserver(
    ([entry]) => {
      if (entry.isIntersecting && hasMoreSections.value && !isLoading.value) {
        loadNextSection();
      }
    },
    {
      root: null, // viewport
      rootMargin: "100px", // trigger early
      threshold: 0.1
    }
  );
  observer.observe(scrollSentinel.value);
});




const loadNextSection = async () => {
  isLoading.value = true;

  try {
    console.log("loading sections", sectionIndex.value);
  
    const response = await homepageService.getSections(sectionIndex.value);
    const data = response.data;
    if (data.section) {
      sections.value.push(data.section);
      sectionIndex.value++;
    }
    
    hasMoreSections.value = data.has_next_section;
  
  } catch (error) {
    console.error("Error loading next section:", error);
    hasMoreSections.value = false; // Stop loading on error
  } finally {
    isLoading.value = false;
  }
};

onMounted(() => {
  
});
</script>

<style scoped>
@import "@/assets/styles/Views/HomepageView.css";
</style>