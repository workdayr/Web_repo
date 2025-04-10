<script setup>
import { defineProps, ref} from 'vue';
import HomepageProductRow from '@/components/Homepage/HomepageProductRow.vue';
defineProps({
  title: String, // Section Title
  icon: String,
  products: Array // List of products
});
const activeIcon = ref(true);
</script>

<template>
  <section class="section-container">
    <div class="section-header">
      <h1 class="section-title">{{ title }}</h1>
      <img v-if="icon && activeIcon" :src="icon" class="section-icon" @error="activeIcon = false">
    </div>
    <HomepageProductRow :products="products"/>
  </section>
</template>

<style scoped>
@import "@/assets/styles/Homepage/HomepageSection.css";
</style>
