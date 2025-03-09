<script setup>
    import {defineProps} from 'vue';
    defineProps({
    title: String
    });
</script>
<template>
    <div class="register__header">
        <img class="back-arrow" src="@/assets/Common/Back.svg" @click="$router.go(-1)">
        <h1 class="register__title">{{title}}</h1>
    </div>
</template>
<style lang="css">
@import "@/assets/styles/Form/FormHeader.css";
</style>