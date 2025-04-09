// stores/homeCacheStore.js
import { defineStore } from 'pinia';
import { ref } from 'vue';

export const useHomeCache = defineStore('homeCache', () => {
  const sections = ref([]);
  const scrollY = ref(0);
  const sectionIndex = ref(0); 

  return {
    sections,
    scrollY,
    sectionIndex
  };
});

