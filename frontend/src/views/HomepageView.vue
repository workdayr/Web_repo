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
import { ref, onMounted, nextTick} from 'vue';
import { onBeforeRouteLeave } from 'vue-router';
import { homepageService } from '@/api/homepageService.js';
import NavbarComponent from '@/components/Layout/NavbarComponent.vue';
import CarouselComponent from '@/components/Layout/CarouselComponent.vue';
import FindBestPrices from '@/components/Homepage/FindBestPrices.vue';
import HomepageSection from '@/components/Homepage/HomepageSection.vue';
import FooterComponent from '@/components/Layout/FooterComponent.vue';
import { useHomeCache } from '@/store/homeCacheStore';

const carouselSlides = ref([
  {
    text: "Compare prices across \ndifferent websites",
    gradient: "linear-gradient(to bottom, #4D1270, #561960)",
    icon: require("@/assets/Carrusel_icons/Slide1.svg"),
    textPosition: "center-left",
    iconPosition: "center-right"
  }
]);

const scrollSentinel = ref(null);
const hasMoreSections = ref(true);
const isLoading = ref(false);

const homeCache = useHomeCache();

const sections = ref(homeCache.sections);
const sectionIndex = ref(homeCache.sectionIndex);

const loadNextSection = async () => {
  isLoading.value = true;

  try {
    const response = await homepageService.getSections(sectionIndex.value);
    const data = response.data;

    if (data.section) {
      sections.value.push(data.section);
      sectionIndex.value++;
    }

    hasMoreSections.value = data.has_next_section;

  } catch (error) {
    console.error("Error loading next section:", error);
    hasMoreSections.value = false;
  } finally {
    isLoading.value = false;
  }
};

onMounted(async () => {
	console.log("length", homeCache.sections.value)
  if (sections.value.length>0) {
	console.log("scrolling");
    await nextTick();
    window.scrollTo(0, homeCache.scrollY);
  } else {
    await loadNextSection();
  }

  const observer = new IntersectionObserver(
    ([entry]) => {
      if (entry.isIntersecting && hasMoreSections.value && !isLoading.value) {
        loadNextSection();
      }
    },
    {
      root: null,
      rootMargin: '100px',
      threshold: 0.1,
    }
  );
  if (scrollSentinel.value) observer.observe(scrollSentinel.value);

  // fallback trigger in case IntersectionObserver fails due to scroll restoration
  await nextTick();
  const checkIfVisible = () => {
    if (!scrollSentinel.value) return;
    const rect = scrollSentinel.value.getBoundingClientRect();
    if (
      rect.top < window.innerHeight &&
      rect.bottom > 0 &&
      hasMoreSections.value &&
      !isLoading.value
    ) {
      loadNextSection();
    }
  };

  checkIfVisible();
  window.addEventListener('scroll', checkIfVisible, { passive: true });
  window.addEventListener('resize', checkIfVisible);
});

onBeforeRouteLeave(() => {
  homeCache.scrollY = window.scrollY;
  homeCache.sections = sections.value;
  homeCache.sectionIndex = sectionIndex.value;
});
</script>


<style scoped>
@import "@/assets/styles/Views/HomepageView.css";
</style>