<script setup>
/* global defineProps */ // 🔹 Solución para ESLint

defineProps({
  title: String,
  value: String,
  percentage: String,
  isPositive: Boolean, // Para indicar si el porcentaje es positivo o negativo
});
</script>

<template>
    <div class="card">
      <div class="card-header">
        <h3>{{ title }}</h3>
      </div>
      <div class="card-body">
        <h2>{{ value }}</h2>
        <span :class="['percentage', { 'positive': isPositive, 'negative': !isPositive }]">
          {{ isPositive ? '▲' : '▼' }} {{ percentage }}
        </span>
      </div>
    </div>
  </template>
  

<style scoped>
@import "@/assets/styles/Dashboard/CardComponent.css";
</style>
