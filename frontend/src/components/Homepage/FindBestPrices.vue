<template>
  <section class="cta-container text-center">
    <div v-if="!authStore.isAuthenticated">
      <h2 class="cta-container__welcomeText" v-scroll-animate>
        Start finding the best prices for you
      </h2>

      <h5 class="welcomeText__description" v-scroll-animate>
        Click and find your best <br> deal
      </h5>
      <button class="cta-button" @click="$router.push('/Register')">Sign up</button>
    </div>

    <h2 v-else class="cta-container__welcomeText" v-scroll-animate>
      {{ 'Welcome ' + authStore.user.first_name }}
    </h2>
  </section>
</template>

<script setup>
import { useAuthStore } from '@/store/useAuthStore';
const authStore = useAuthStore();


const vScrollAnimate = {
  mounted(el) {
    const observer = new IntersectionObserver(
      (entries, observer) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            el.classList.add("visible");
            observer.unobserve(el); // Stop observing after it's visible
          }
        });
      },
      { threshold: 0.2 } // Trigger when 20% of the element is visible
    );

    observer.observe(el);
  },
};
</script>

<style scoped>
@import "@/assets/styles/Homepage/FindBestPrices.css";
</style>
