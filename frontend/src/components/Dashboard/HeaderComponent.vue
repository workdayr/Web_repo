<template>
    <div class="Header__container" :style="{paddingBottom : paddingBottom, textAlign : align,}">
        <h1 class="Header__text" :style="{fontSize : fontSize, color: color,}">{{ text }}</h1>
    </div>
</template>
<script setup>
import { defineProps } from 'vue';
defineProps({
    text: { type: String, required: true, },
    fontSize: { type: String, default: 'x-large', },
    color: { type: String, default: '#fff', },
    paddingBottom: { type: String, default: '20px', },
    align: { type: String, default: 'left' },
});

</script>
<style scoped>
.Header__container {
    width: 100%;
}

.Header__text {
    margin: 0;
}
</style>