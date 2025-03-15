<template>
  <div id="carousel" class="carousel slide" data-bs-ride="carousel" data-bs-interval="5000">
    <div class="carousel-inner">
      <div v-for="(slide, index) in slides" :key="index" class="carousel-item" :class="{ active: index === 0 }">
        <div class="slide-content" :style="{ background: slide.gradient }">
          <div class="text-container" :class="slide.textPosition">
            <h1 v-html="formatText(slide.text)" class="slide-text"></h1>
          </div>
          <img v-if="slide.icon" :src="slide.icon" alt="Slide Icon" class="slide-icon" :class="slide.iconPosition" loading="lazy"/>
        </div>
      </div>
    </div>
    <button class="carousel-control-prev" type="button" data-bs-target="#carousel" data-bs-slide="prev">
      <span class="carousel-control-prev-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Previous</span>
    </button>
    <button class="carousel-control-next" type="button" data-bs-target="#carousel" data-bs-slide="next">
      <span class="carousel-control-next-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Next</span>
    </button>
  </div>
</template>

<script setup>
import { defineProps } from 'vue';

defineProps({
  slides: {
    type: Array,
    required: true,
  }
});

const formatText = (text) => {
      return text.replace(/\n/g, '<br>'); // Reemplaza \n con <br>
    }
</script>

<style scoped>
@import "@/assets/styles/Layout/CarouselComponent.css";
</style>
