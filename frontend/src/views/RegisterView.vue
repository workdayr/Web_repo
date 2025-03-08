<script setup>
import FormHeader from '@/components/Form/FormHeader.vue';
import RegisterFrom from '@/components/Register/RegisterForm.vue';
</script>

<template>
    
    <div class="register__background">
        <img class="background__shape1" src="@/assets/svg/Vector.svg" alt="Vector">
        <img class="background__shape2" src="@/assets/svg/backgroundShape.svg" alt="Background Shape">
    </div>
    
    <div class="register__container">
		<FormHeader title="Register"/>
        <RegisterFrom/>
        <p class="register__text">
            By clicking "Create account" you agree to our 
            <a href="/terms" class="register__link">terms</a> and 
            <a href="/privacy-policy" class="register__link">privacy policy</a>.
        </p>

        
    </div>
</template>

<style scoped>
@import "@/assets/styles/Views/RegisterView.css";
</style>