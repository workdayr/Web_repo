<template>
    <div v-if="show" class="error-container">
      <div class="error-content">
        <div class="error-icon">
          <img :src="require('@/assets/Common/exclamation.svg')" alt="Error" />
        </div>
        <div class="error-message">
          {{ message }}
        </div>
        <button @click="close" class="error-close">
          <img :src="require('@/assets/Common/close.svg')" alt="Close" />
        </button>
      </div>
    </div>
  </template>
  
  <script setup>
import { defineProps, defineEmits } from 'vue';

defineProps({
  message: {
    type: String,
    default: 'Invalid Credentials. Email or Password Incorrect'
  },
  show: {
    type: Boolean,
    default: false
  }
})

const emit = defineEmits(['close']);

function close() {
  emit('close')
}
</script>

  
  <style scoped>
 @import "@/assets/styles/Common/ErrorMessage.css";
  </style>