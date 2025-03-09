<script setup>
import { ref, defineProps} from 'vue';
import router from '@/router';
defineProps({
  name: String,
});

const isSelected = ref(false);

const toggleSelection = () => {
  isSelected.value = !isSelected.value;
};
const redirect = () => {
    router.push('/Dashboard');
};

</script>

<template>
  <div 
    class="sideMenu__option"
    :class="{ active: isSelected }"
    @click="toggleSelection(); redirect();"
    
  >
    <p class="sideMenu__option-text">{{ name }}</p>
  </div>
</template>

<style scoped>
@import "@/assets/styles/Dashboard/OptionComponent.css";
</style>