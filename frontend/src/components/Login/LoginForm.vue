<script setup>
import { ref } from 'vue';
import FormInput from '@/components/Form/FormInput.vue';
import FormSubmitButton from '@/components/Form/FormSubmitButton.vue';
import { useRegisterValidation } from '@/composables/useRegisterValidation';
import { useRouter } from 'vue-router';
import { useAuth } from "@/composables/useAuth";

const router = useRouter(); 

const form = ref({
	email: '',
	password: ''
});

const submitted = ref(false);
const sent = ref(false);

const { validFields, errorMessage } = useRegisterValidation(form);
const { login } = useAuth(); 

// submit form function
const submitForm = async () => {
	submitted.value = true;
	// Client form validation
	let isValid = Object.values(validFields.value).every(Boolean);
	if (!isValid || sent.value) {
		return;
	}
	sent.value = true;

	const payload = {
		email: form.value.email,
		password: form.value.password,
	};

	try {
		await login(payload);
		router.push('/');
	} catch (error) {
		if (error.response) {
			const errorData = error.response.data;
			console.error('Error response received:', errorData);
			return error.response;
		} else if (error.request) {
			console.error('No response received:', error.request);
			return error.request;
		} else {
			console.error('Error setting up the request:', error.message);
			return error;
		}
	} finally {
		sent.value = false; // Rehabilitamos el botón después de la petición
	}
};
</script>

<template>
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