<template>
    <div class="price-card">
      <h2 class="store-name">{{ store }}</h2>
      <p class="price-display">
        ${{ price }}<span class="currency">MXN</span>
      </p>
      <ul class="feature-list">
        <li v-for="(feature, index) in features" :key="index" class="feature-item">
          <span class="checkmark">✔</span>
          <span class="feature-text">{{ feature }}</span>
        </li>
      </ul>
      <button class="buy-button">Buy now</button>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      store: String,
      price: Number,
      features: Array
    }
  };
  </script>
  
  <style scoped>
   @import "@/assets/styles/Product/PriceCard.css";
  </style>