<script setup>
import {defineProps, onMounted, ref} from 'vue';
const props = defineProps({
    text:String,
    focus: Boolean
});

const inputRef = ref(null);

const focusInput = () => {
    inputRef.value?.focus();
};

onMounted(() => {
  if(props.focus) focusInput();
});
</script>

<template>
    <div class="searchbar-container">
    <img class="search-icon" src="@/assets/Common/SearchIcon.svg" alt="Search Icon">
    <input class="searchbar" type="search" :placeholder="text" aria-label="Search" @blur="$emit('blur')" ref="inputRef">
  </div>
</template>

<style scoped>
@import "@/assets/styles/UI/SearchbarComponent.css";
</style>