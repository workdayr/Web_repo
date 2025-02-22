<template>
  <section class="cta-container text-center">
    <h2 class="cta-container__welcomeText" v-scroll-animate>
      Start finding the best prices for you
    </h2>
    <h5 class="welcomeText__description" v-scroll-animate>Click and find your best <br> deal</h5>
    <button class="cta-button">Sign up</button>
  </section>
</template>

<script>
export default {
  directives: {
    'scroll-animate': {
      mounted(el) {
        const observer = new IntersectionObserver(
          (entries) => {
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
    },
  },
};

</script>

<style scoped>
@import "@/assets/styles/FindBestPrices.css";

</style>