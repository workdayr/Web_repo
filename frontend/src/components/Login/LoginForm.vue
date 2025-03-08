<script setup>
import { ref } from 'vue';
import FormInput from '../Form/FormInput.vue';
import FormSubmitButton from '../Form/FormSubmitButton.vue';
import { useRegisterValidation } from '@/composables/useRegisterValidation';

const form = ref({
    username: '',
    passwordLogin: '',
    rememberMe: false,
});
const {validFields, errorMessage} = useRegisterValidation(form, 'login');
const submitted = ref(false);


const submitForm = () => {
    submitted.value = true;

    if (validFields.value.username && validFields.value.passwordLogin) {
        console.log('Login successful!', form.value);
    }
};  
</script>

<template>
        <form @submit.prevent="submitForm">
            <div class="login__input--container">
                <FormInput id="login__input--username" v-model="form.username" :src="require('@/assets/Form/Full_name.svg')"
                    :placeholder="'Username'" :is-valid="validFields.username" :submitted="submitted"
                    :error-message="errorMessage.username" />
                <FormInput id="login__input--password" v-model="form.passwordLogin" :src="require('@/assets/Form/Password.svg')"
                    :placeholder="'Password'" type="password" :is-valid="validFields.passwordLogin" :submitted="submitted"
                    :error-message="errorMessage.passwordLogin" />
            
            <div id="login__inputs">
                <label>
                    <input id="login__input--rememberMe" type="checkbox" v-model="form.rememberMe">
                    <span class="input__rememberMe--label">Remember me</span>
                </label>
                <a class="login__link--forgotPw" @click="$router.push('/')" >Forgot password?</a>
            </div>

            <FormSubmitButton text="NEXT" />
        </div>
        </form>
</template>
<style scoped>
@import "@/assets/styles/Login/LoginForm.css"
</style>