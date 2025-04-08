<template>
  <div class="price-card">
    <div v-if="price === 'Cargando...'">
      <p>Cargando...</p>
    </div>
    <div v-else>
      <p>{{ price }}</p>
      <p>{{ store }}</p>
      <p>{{ features }}</p>
    </div>
  </div>
</template>

<script setup>
import { defineProps } from 'vue';
defineProps({
  store: String,
  price: String,
  features: String,
});
</script>

  
  <style scoped>
   @import "@/assets/styles/Product/PriceCard.css";
  </style>