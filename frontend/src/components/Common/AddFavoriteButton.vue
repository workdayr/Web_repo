<script setup>
import { defineProps, defineEmits } from 'vue';

const props = defineProps({
  isFollowed: Boolean,
});

const emit = defineEmits(['update:isFollowed']);

const addToFavorites = () => {
  emit('update:isFollowed', !props.isFollowed);
};
</script>

<template>
  <button class="fav__button" @click="addToFavorites">
    <svg
      class="fav__image"
      :class="{ followed: isFollowed }"
      width="26"
      height="25"
      viewBox="0 0 26 25"
      xmlns="http://www.w3.org/2000/svg"
    >
      <path
        d="M14.2896 2.15019L17.0326 6.76796C17.3834 7.35859 17.9618 7.77882 18.6319 7.92996L23.8713 9.11168C24.9817 9.36212 25.4194 10.7095 24.6684 11.5647L21.1242 15.6004C20.6709 16.1166 20.45 16.7965 20.5133 17.4805L21.0085 22.8287C21.1134 23.9621 19.9673 24.7948 18.9218 24.3447L13.9885 22.2211C13.3575 21.9495 12.6425 21.9495 12.0115 22.2211L7.0782 24.3447C6.03271 24.7948 4.88657 23.9621 4.99151 22.8287L5.48669 17.4805C5.55002 16.7965 5.32909 16.1166 4.87579 15.6004L1.33164 11.5647C0.580552 10.7095 1.01834 9.36212 2.12868 9.11168L7.36806 7.92996C8.03819 7.77882 8.61659 7.35858 8.96742 6.76796L11.7104 2.15019C12.2916 1.17158 13.7084 1.17158 14.2896 2.15019Z"
        stroke="white"
      />
    </svg>
  </button>
</template>

<style scoped>
@import '@/assets/styles/Common/AddFavoriteButton.css';
</style>