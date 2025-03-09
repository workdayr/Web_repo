<template>
  <section id="Homepage">
    <!-- Navbar -->
    <Navbar />

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
import Navbar from '@/components/Layout/Navbar.vue';
import CarouselComponent from '@/components/Layout/CarouselComponent.vue'; // Asegurando que coincida el nombre del componente
import BprcsLogo from '@/assets/Bprcs_logo.png';
import ProductsComponent from '@/components/Homepage/ProductsComponent.vue';
import FooterComponent from '@/components/Layout/Footer.vue';
import OpinionsComponent from '@/components/Homepage/OpinionsComponent.vue';
import FindBestPrices from '@/components/Homepage/FindBestPrices.vue';
export default {
  name: 'HelloWorld',
  components: {
    Navbar,
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
/* Estilos para la Navbar */
@import "@/assets/styles/Layout/NavbarComponent.css";
/* Asegura que se carguen los estilos */

/* Corrección para navbar: fixed y ajuste de fondo */
.Homepage__navBar {
  height: 60px;
  display: flex;
  top: 0;
  width: 100%;
  position: absolute;
  background-color: rgba(0, 0, 0, 0.2);
  /* Fondo para mayor visibilidad */
  z-index: 1000;
  /* Se mantiene sobre el carrusel */
}

/* Corrección del buscador */
.navBar__searchBar {
  border-radius: 20px;
  border: 1px solid #FFFF;
  width: 422px;
  height: 30px;
  margin: 12px;
  margin-left: 100px;
}

/* Ajuste del logo */
.navBar__BprcsLogo img {
  display: inline-block;
  width: 120px;
  height: auto;
  max-width: 100%;
  padding-top: 12px;
  margin-left: 60px;
}
</style>
