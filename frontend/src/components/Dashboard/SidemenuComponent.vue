<script setup>
import OptionComponent from '@/components/Dashboard/OptionComponent.vue';
import SearchbarComponent from '@/components/UI/SearchbarComponent.vue';
import LogoComponent from '../UI/LogoComponent.vue';
import { ref, defineEmits } from 'vue';

const emit = defineEmits(['select-section']);
const isOpen = ref(false);
const toggleMenu = () => (isOpen.value = !isOpen.value);

const sections = ["User Analytics", "Products", "Notifications", "Users"];

</script>
<template>
  <button class="menu-toggle" @click="toggleMenu">☰</button>
  <div :class="['overlay', { active: isOpen }]"></div>

  <div :class="['sideMenu__container', { active: isOpen }]">
    <LogoComponent class="sideMenu__logo" :render-title="true"/>
    <div class="separation-line">.</div>
    <SearchbarComponent text="Search for..." class="sideMenu__searchbar" />
    <div class="sideMenu__options-container">
      <OptionComponent v-for="section in sections" :key="section" :name="section"
        @click="emit('select-section', section)" />
    </div>
  </div>
</template> 

<style scoped>
@import "@/assets/styles/Dashboard/SidemenuComponent.css";
</style>