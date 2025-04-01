<template>
    <div class="faq-item">
      <button @click="isOpen = !isOpen" class="faq-question">
        <span>{{ question }}</span>
        <span class="icon" :class="{ 'rotate': isOpen }">▼</span>
      </button>
      <div v-if="isOpen" class="faq-answer">
        <p>{{ answer }}</p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      question: String,
      answer: String
    },
    data() {
      return {
        isOpen: false
      };
    }
  };
  </script>
  
  <style scoped>
  @import "@/assets/styles/UI/FaqItemComponent.css";
  </style>
  