<script setup>
import { defineProps} from 'vue';
import router from '@/router';
defineProps({
  name: String,
  isSelected: Boolean,
});

const redirect = () => {
    router.push('/Dashboard');
};

</script>

<template>
  <div 
    class="sideMenu__option"
    :class="{ active: isSelected }"
    @click="redirect();"
    
  >
    <p class="sideMenu__option-text">{{ name }}</p>
  </div>
</template>

<style scoped>
@import "@/assets/styles/Dashboard/OptionComponent.css";
</style>