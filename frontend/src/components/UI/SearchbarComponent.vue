<script setup>
import { defineProps, onMounted, ref } from 'vue';
const props = defineProps({
  text: { type: String, required: true, default: 'Search' },
  fontSize: { type: String, default: 'x-small', },
  color: { type: String, default: '#AEB9E1', },
  background: { type: String, default: '#321647', },
  paddingLeft: { type: String, default: '35px', },
  width: { type: String, default: '230px' },
  height: { type: String, default: '40px' },
  marginLeft: { type: String, default: '0px' },
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
  <div class="searchbar-container" :style="{ marginLeft: marginLeft, width: width, height: height }">
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