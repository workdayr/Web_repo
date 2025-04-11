<script setup>
import { ref } from 'vue';
import FormInput from '@/components/Form/FormInput.vue';
import FormSubmitButton from '@/components/Form/FormSubmitButton.vue';
import ErrorMessage from '@/components/Common/ErrorMessage.vue'; // Asegúrate de importar tu componente
import { useRegisterValidation } from '@/composables/useRegisterValidation';
import { useRouter } from 'vue-router';
import { useAuth } from "@/composables/useAuth";

const router = useRouter();

const form = ref({
	email: '',
	password: '',
	rememberMe: false,
});

const submitted = ref(false);
const sent = ref(false);

const showError = ref(false);
const errorText = ref('');

const { validFields, errorMessage } = useRegisterValidation(form);
const { login } = useAuth();

const submitForm = async () => {
	submitted.value = true;

	const isValid = Object.values(validFields.value).every(Boolean);
	if (!isValid || sent.value) return;

	sent.value = true;

	const payload = {
		email: form.value.email,
		password: form.value.password,
		rememberMe: form.value.rememberMe
	};

	try {
		await login(payload);
		router.push('/');
	} catch (error) {
		showError.value = true;
		const status = error.response?.status;

		if (status === 401) {
			errorText.value = 'Invalid Credentials. Email or Password Incorrect';
		} else if (status === 404) {
			errorText.value = 'Login service not found. Please contact support.';
		} else {
			errorText.value = 'An unexpected error occurred. Please try again.';
		}
	} finally {
		sent.value = false;
	}
};

const closeError = () => {
	showError.value = false;
};
</script>


<template>
	<ErrorMessage :message="errorText" :show="showError" @close="closeError" />
	<form class="login__form" @submit.prevent="submitForm">
		
		<FormInput id="login__input--email" v-model="form.email" :src="require('@/assets/Form/Email.svg')"
			:placeholder="'Email'" :is-valid="validFields.email" :submitted="submitted"
			:error-message="errorMessage.email" />
		<FormInput id="login__input--password" v-model="form.password" :src="require('@/assets/Form/Password.svg')"
			:placeholder="'Password'" type="password" :is-valid="validFields.password" :submitted="submitted"
			:error-message="errorMessage.password" />

		<div id="login__inputs">
			<label>
				<input id="login__input--rememberMe" type="checkbox" v-model="form.rememberMe">
				<span class="input__rememberMe--label">Remember me</span>
			</label>
			<a class="login__link--forgotPw" @click="$router.push('/')">Forgot password?</a>
		</div>

		<FormSubmitButton text="NEXT" :sent="sent" />
	</form>
</template>
<style scoped>
@import "@/assets/styles/Login/LoginForm.css"
</style>