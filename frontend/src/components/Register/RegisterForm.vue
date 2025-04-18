<script setup>
import { ref } from 'vue';
import AppInput from '@/components/Form/FormInput.vue';
import AppSubmitButton from '@/components/Form/FormSubmitButton.vue';
import { useRegisterValidation } from '@/composables/useRegisterValidation';
import { useRouter } from 'vue-router';
import { useAuth } from "@/composables/useAuth";
import ErrorMessage from '../Common/ErrorMessage.vue';

const router = useRouter();
const states = ['State A', 'State B', 'State C'];
const showError = ref(false);
const errorText = ref('');
const handleCloseError = () => {
	showError.value = false;
	errorText.value = '';
};

const form = ref({
	fullName: '',
	email: '',
	password: '',
	confirmPassword: '',
	birthday: '',
	state: ''
});

const submitted = ref(false);
const sent = ref(false);
const { validFields, errorMessage } = useRegisterValidation(form);
const { register } = useAuth();
// submit form function	
const submitForm = async () => {
	submitted.value = true;

	// Client form validation
	let isValid = Object.values(validFields.value).every(Boolean);
	if (!isValid || sent.value) {
		return;
	}

	const payload = {
		username: form.value.email,
		first_name: form.value.fullName.split(' ')[0],
		last_name: form.value.fullName.split(' ').slice(1).join(' ') || "",
		email: form.value.email,
		password: form.value.password,
		date_of_birth: form.value.birthday,
		state: form.value.state
	};

	try {
		sent.value = true;
		await register(payload);
		// add user success message
		router.push('/');

	} catch (error) {
		console.error('Error al registrar usuario', error);
		showError.value = true;

		if (error.response) {
			const errorData = error.response.data;

			if (errorData?.email?.[0]?.includes('already')) {
				errorText.value = 'This email is already registered. Try logging in.';
			} else if (errorData?.username?.[0]?.includes('already')) {
				errorText.value = 'Username is already taken.';
			} else {
				errorText.value = 'Registration failed. Please check your input.';
			}
			return error.response;
		} else if (error.request) {
			errorText.value = 'No response from server. Please try again later.';
			return error.request;
		} else {
			errorText.value = 'Unexpected error. Please try again.';
			return error;
		}

	} finally {
		sent.value = false; // Reset sent state
	}
};
</script>

<template>
	<ErrorMessage :show="showError" :message="errorText" @close="handleCloseError" />

	<form class="register__form" @submit.prevent="submitForm">

		<AppInput v-model="form.fullName" :src="require('@/assets/Form/FullName.svg')" placeholder="Full Name"
			:is-valid="validFields['fullName']" :submitted="submitted" :error-message="errorMessage['fullName']" />
		<AppInput v-model="form.email" :src="require('@/assets/Form/Email.svg')" placeholder="Email" type="email"
			:is-valid="validFields['email']" :submitted="submitted" :error-message="errorMessage['email']" />
		<AppInput v-model="form.password" :src="require('@/assets/Form/Password.svg')" placeholder="Password"
			type="password" :is-valid="validFields['password']" :submitted="submitted"
			:error-message="errorMessage['password']" />
		<AppInput v-model="form.confirmPassword" :src="require('@/assets/Form/Password.svg')"
			placeholder="Confirm Password" type="password" :is-valid="validFields['confirmPassword']"
			:submitted="submitted" :error-message="errorMessage['confirmPassword']" />

		<div class="register__row">
			<AppInput v-model="form.birthday" :src="require('@/assets/Form/Birthday.svg')" placeholder="Birthday"
				type="date" :is-valid="validFields['birthday']" :submitted="submitted"
				:error-message="errorMessage['birthday']" />
			<AppInput v-model="form.state" :src="require('@/assets/Form/State.svg')" placeholder="State" type="select"
				:options="states" :is-valid="validFields['state']" :submitted="submitted"
				:error-message="errorMessage['state']" />
		</div>

		<AppSubmitButton text="Create account" :sent="sent" />
	</form>
</template>

<style lang="css">
@import "@/assets/styles/Register/RegisterForm.css";
</style>
