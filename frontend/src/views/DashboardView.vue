<script setup>
import OptionComponent from '@/components/UI/OptionComponent.vue';
import SearchbarComponent from '@/components/UI/SearchbarComponent.vue';
import { ref } from 'vue';
const isOpen = ref(false);

const toggleMenu = () => {
  isOpen.value = !isOpen.value;
};

</script>
<template>
    <button class="menu-toggle" @click="toggleMenu">☰</button>
    <div :class="['overlay', { active: isOpen }]"></div>

    <div :class="['sideMenu__container', { active: isOpen }]">
    <div class="sideMenu__header">
      <img class="bprcs-logo" src="@/assets/Common/Logo.svg" alt="Logo">
      <h1 class="sideMenu__title">Bprcs</h1>
    </div>
        <div class="separation-line">.</div>
        <SearchbarComponent text="Search for..." />
        <div class="sideMenu__options-container">
            <OptionComponent name="User Analytics" />
            <OptionComponent name="Products" />
            <OptionComponent name="Notification & Alert Statistics" />
            <OptionComponent name="Pricing" />
            <OptionComponent name="Settings" />
        </div>
    </div>
</template>

<style scoped>
@import "@/assets/styles/Views/DashboardView.css";
</style>