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
const sent = ref(false);

const submitForm = () => {
    submitted.value = true;

    if (validFields.value.username && validFields.value.passwordLogin) {
        sent.value = true;
        console.log('Login successful!', form.value);
    }
};  
</script>

<template>
        <form class="login__form" @submit.prevent="submitForm" >
                <FormInput id="login__input--username" v-model="form.username" :src="require('@/assets/Form/FullName.svg')"
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

            <FormSubmitButton text="NEXT" :sent="sent"/>
        </form>
</template>
<style scoped>
@import "@/assets/styles/Login/LoginForm.css"
</style>