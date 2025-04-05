<script setup>
import { defineProps, onMounted, ref } from 'vue';
const props = defineProps({
  text: { type: String, required: true, default: 'Search' },
  focus: { type: Boolean, default: false },
});

const inputRef = ref(null);

const focusInput = () => {
  inputRef.value?.focus();
};

onMounted(() => {
  if (props.focus) focusInput();
});
</script>

<template>
  <div class="searchbar-container">
    <img class="search-icon" src="@/assets/Common/SearchIcon.svg" alt="Search Icon">
    <input class="searchbar" :style="{
      fontSize: fontSize, color: color, backgroundColor: background,
      paddingLeft: paddingLeft,
    }" type="search" :placeholder="text" aria-label="Search" @blur="$emit('blur')" ref="inputRef">

  </div>
</template>

<style scoped>
@import "@/assets/styles/UI/SearchbarComponent.css";
</style>