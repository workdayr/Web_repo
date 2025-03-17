<template>
    <div class="logo__container" @click="$router.push('/')">
        <img class="bprcs-logo" src="@/assets/Common/Logo.svg" alt="Logo">
        <h1 v-if="renderTitle" class="logo__title">Bprcs</h1>
    </div>
</template>
<script setup>
import { defineProps } from 'vue';
defineProps({
    renderTitle: Boolean
});
</script>

<style scoped>
@import "@/assets/styles/UI/LogoComponent.css";
</style>
