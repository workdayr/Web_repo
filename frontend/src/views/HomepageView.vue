<template>
  <section id="Homepage">
    <!-- Navbar -->
    <NavbarComponent :is-always-compact="false"/>

    <!-- Ajuste para que el carrusel no se superponga con el navbar -->
    <div style="margin-top: 60px;">
      <CarouselComponent />
    </div>

    <FindBestPrices />
    <div>
      <ProductsComponent />
    </div>

    <OpinionsComponent />

    <FooterComponent />




  </section>
</template>

<script>
import NavbarComponent from '@/components/Layout/NavbarComponent.vue';
import CarouselComponent from '@/components/Layout/CarouselComponent.vue'; // Asegurando que coincida el nombre del componente
import BprcsLogo from '@/assets/Bprcs_logo.png';
import ProductsComponent from '@/components/Homepage/ProductsComponent.vue';
import FooterComponent from '@/components/Layout/Footer.vue';
import OpinionsComponent from '@/components/Homepage/OpinionsComponent.vue';
import FindBestPrices from '@/components/Homepage/FindBestPrices.vue';
export default {
  name: 'HelloWorld',
  components: {
    NavbarComponent,
    CarouselComponent, // Antes estaba como "Carrusel", ahora coincide con el import
    ProductsComponent,
    FooterComponent,
    OpinionsComponent,
    FindBestPrices,
  },
  data() {
    return {
      BprcsLogo
    };
  }
};
</script>


<style scoped>
</style>
