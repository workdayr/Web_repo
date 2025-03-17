<template>
    <div class="Header__container">
        <h1 class="Header__text">{{ text }}</h1>
    </div>
</template>
<script setup>
import { defineProps } from 'vue';
defineProps({
    text:String
})

</script>
<style scoped>
    .Header__container{
        padding-bottom: 20px;
    }
    .Header__text{
        font-size: x-large;
        color: #fff;
    }
</style>