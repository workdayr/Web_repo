<script setup>
import { defineProps} from 'vue';
import HomepageProductRow from '@/components/Homepage/HomepageProductRow.vue';
defineProps({
  title: String, // Section Title
  products: Array // List of products
});
</script>

<template>
  <section class="section">
    <h1 class="section-title">{{ title }}</h1>
    <HomepageProductRow :products="products"/>
  </section>
</template>

<style scoped>
@import "@/assets/styles/Homepage/HomepageSection.css";
</style>
