<template>
  <section id="Homepage">
    <nav class="Homepage__navBar">
      <a class="navBar__BprcsLogo" href="http://localhost:8080/?#">
        <img :src="BprcsLogo" alt="Bprcs_logo">
      </a>
      <input class="navBar__searchBar" type="search" placeholder="Search" aria-label="Search">
      <li class="navBar__li--FQA">FQA</li>
      <li class="navBar__li--Explore">Explore</li>
      <div class="navBar__buttons">
        <button class="navBar__buttons--SignUp">Sign Up</button>
        <button class="navBar__buttons--Login">Log In</button>
      </div>
    </nav>
    <Carrusel /> <!-- Aquí colocas el componente Carrusel -->
  </section>
</template>

<script>
import BprcsLogo from '@/assets/Bprcs_logo.png'; // Importa el logo
import Carrusel from '@/components/CarouselComponent.vue'; // Importa el componente Carrusel

export default {
  name: 'HelloWord', // Nombre del componente
  components: {
    Carrusel // Registra el componente Carrusel
  },
  data() {
    return {
      BprcsLogo // Asocia el logo al componente
    };
  }
};
</script>

<style scoped>
/* Estilos específicos para este componente */
.Homepage__navBar {
  height: 60px;
  display: flex;
  position: absolute;
  top: 29.73px;
}

.navBar__searchBar {
  border-radius: 20px;
  border: 1px solid #FFFF;
  width: 422px;
  height: 30px;
  margin: 12px;
  margin-left: 100px;
}

.navBar__BprcsLogo img {
  display: inline-block;
  width: 120px;
  height: auto;
  max-width: 100%;
  padding-top: 12px;
  margin-left: 60px;
}
</style>
