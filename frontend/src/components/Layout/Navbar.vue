<template>
  <nav class="Homepage__navBar">
    <a class="navBar__BprcsLogo" href="http://localhost:8080/?#">
      <img :src="BprcsLogo" alt="Bprcs_logo">
    </a>
    <input class="navBar__searchBar" type="search" placeholder="Search" aria-label="Search">
    <li class="navBar__li--FQA">FQA</li>
    <li class="navBar__li--Explore">Explore</li>
    <div class="navBar__buttons">
      <button @click="$router.push('/Register')" class="navBar__buttons--SignUp">Sign Up</button>
      <button @click="$router.push('/login')" class="navBar__buttons--Login">Log In</button>
    </div>
  </nav>
</template>

<script>
import BprcsLogo from '@/assets/Bprcs_logo.png';

export default {
  name: 'NavbarComponent',
  data() {
    return {
      BprcsLogo
    };
  }
};
</script>

<style scoped>
@import "@/assets/styles/Layout/NavbarComponent.css"; /* Cambia si tu archivo tiene otro nombre */
</style>
