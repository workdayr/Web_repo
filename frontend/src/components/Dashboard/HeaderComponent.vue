<template>
    <div class="Header__container" :style="{paddingBottom : paddingBottom, textAlign : align, paddingRight:paddingRight}">
        <h1 v-if="screenWidth >= 768" class="Header__text" :style="{fontSize : fontSize, color: color,}">{{ text }}</h1>
        <h1 v-if="screenWidth < 768" class="Header__text" :style="{fontSize : responsiveFontSize, color: responsiveColor,}">{{ text }}</h1>
    </div>
</template>
<script setup>
import { defineProps, ref, onMounted, onUnmounted } from 'vue';
const screenWidth = ref(window.innerWidth)


defineProps({
    text: { type: String, required: true, },
    fontSize: { type: String, default: 'x-large', },
    color: { type: String, default: '#fff', },
    paddingBottom: { type: String, default: '20px', },
    paddingRight:{type:String, default: '0px'},
    align: { type: String, default: 'left'},

    responsiveText: { type: String, required: true, },
    responsiveFontSize: { type: String, default: 'medium', },
    responsiveColor: { type: String, default: '#fff', },
});


const updateScreenWidth = () => {
  screenWidth.value = window.innerWidth;
};

onMounted(() => {
  window.addEventListener('resize', updateScreenWidth);
});

onUnmounted(() => {
  window.removeEventListener('resize', updateScreenWidth);
});


</script>
<style scoped>
.Header__container {
    width: auto;
}

.Header__text {
    margin: 0;
}
</style>