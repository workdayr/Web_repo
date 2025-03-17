<script setup>
import {ref, defineAsyncComponent} from 'vue';
import SidemenuComponent from '@/components/Dashboard/SidemenuComponent.vue';
const sections =  {
  "User Analytics": defineAsyncComponent(() => import('@/components/Dashboard/Sections/UseranalyticsSection.vue')),

}
const activeSection = ref(null);
const openSection = (section) => (activeSection.value = section);

</script>
<template>
<SidemenuComponent @select-section="openSection"/>
<div class="dashboard__content">
    <component v-if="activeSection" :is="sections[activeSection]" />
</div>
</template>

<style scoped>
@import "@/assets/styles/Views/DashboardView.css";
</style>