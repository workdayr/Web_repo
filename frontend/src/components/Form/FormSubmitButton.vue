<script setup>
    import {defineProps} from 'vue';
    defineProps({
        text: String,
        sent: Boolean
    });
</script>
<template>
    <div class="register__button-container">
        <button type="submit" class="register__button">
            <span v-if="!sent"> {{text}}</span> 
            <span class="loader" v-else></span>
        </button>
    </div>
</template>
<style lang="css">
@import "@/assets/styles/Form/FormSubmitButton.css";
</style>