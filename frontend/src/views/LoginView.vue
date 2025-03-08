<script setup>
import FormHeader from '@/components/Form/FormHeader.vue';
import LoginForm from '@/components/Login/LoginForm.vue';
</script>

<template>
    <div id="login__background">
        <img class="background__shape1" src="@/assets/Form/BackgroundShape2.svg" alt="Vector">
        <img class="background__shape2" src="@/assets/Form/BackgroundShape1.svg" alt="backgroundShape">
    </div>

    <div class="login__form--container">
        <FormHeader title="Log In"/>
        <LoginForm />

        <div id="login__other-login-options">
            <p>Other <span class="login__other-login-options--highlited-word">Login</span> options</p>
            <div class="other-login-options__icons">
                <img class="GoogleIcon" src="@/assets/Login/GoogleLogo.svg" alt="Google">
                <img class="FacebookIcon" src="@/assets/Login/FacebookLogo.svg" alt="Facebook">
                <img class="AppleIcon" src="@/assets/Login/AppleLogo.svg" alt="Apple">
            </div>
            <div id="create-account-container">
                <img class="userIcon" src="@/assets/Form/FullName.svg" alt="UserIcon">
                <a class="create-account-container__header">Create account</a>
            </div>
        </div>
    </div>
</template>

<style scoped>
@import "@/assets/styles/Views/LoginView.css";
</style>