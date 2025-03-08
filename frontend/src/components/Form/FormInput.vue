<script setup>
import {defineModel, defineProps} from 'vue';

defineProps({
    modelValue: String,
    src: String,
    placeholder: String,
    type: { type: String, default: 'text' },
    options: { type: Array, default: () => [] },
    isValid: Boolean,
    submitted: Boolean,
    errorMessage: {type: String,default: '',},
});
const model = defineModel('modelValue');

</script>

<template>
    <div>
        <div class="register__input-group" >
            <img v-if="src" class="register__icon" :src="src" alt="icon">
            <input v-if="type!=='select'" class="register__input" :class="{ 'valid': isValid, 'has-value': modelValue}" v-model="model" :type="type" :placeholder="placeholder">
            <select v-else class="register__input" v-model="model" :class="{ 'valid': isValid }" :type="type" :placeholder="placeholder" >
                <option value="" disabled>{{placeholder}}</option>
                <option v-for="option in options" :key="option" :value="option">{{ option }}</option>     
                
            </select>
            <img v-if="type=='select'" id="arrow" class="register__icon" src="@/assets/Register_icons/Select_arrow.svg" alt="icon">      
        </div>
        <Transition name="fade">
            <p v-if="!isValid && submitted" class="error__message">{{errorMessage}}</p>
        </Transition>
    </div>
</template>

<style lang="css">
@import "@/assets/styles/Form/FormInput.css";
</style>
