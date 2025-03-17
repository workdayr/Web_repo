<script setup>
import { ref } from 'vue';
import axios from 'axios';
import AppInput from '@/components/Form/FormInput.vue';
import AppSubmitButton from '@/components/Form/FormSubmitButton.vue';
import { useRegisterValidation } from '@/composables/useRegisterValidation';
import { hashPassword } from '@/utils/hashUtils';
import Swal from 'sweetalert2';
import { useRouter } from 'vue-router';

const router = useRouter(); 

const states = ['State A', 'State B', 'State C'];

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

// backend URL
const API_URL = 'http://127.0.0.1:8000/api/users/';

// submit form function
const submitForm = async () => {
	submitted.value = true;

	// Client form validation
	let isValid = Object.values(validFields.value).every(Boolean);
	if (!isValid || sent.value) {
		return;
	}
	sent.value = true;

	const hashedPassword = hashPassword(form.value.password);

	const payload = {
		username: form.value.email, // Se usa el email como username
		first_name: form.value.fullName.split(' ')[0], // Extraer primer nombre
		last_name: form.value.fullName.split(' ').slice(1).join(' ') || "", // Extraer el apellido si existe
		email: form.value.email,
		password: hashedPassword, // Se envía la contraseña en SHA-256 con sal
		date_of_birth: form.value.birthday,
		state: form.value.state // Enviar el estado
	};

	try {
		Swal.fire({
			title: 'Enviando datos...',
			text: 'Por favor espera mientras enviamos tus datos.',
			showConfirmButton: false,
			allowOutsideClick: false,
			didOpen: () => {
				Swal.showLoading();
			}
		});

		console.log('Enviando datos al servidor...', payload);
		const response = await axios.post(API_URL, payload);

		console.log('Registro exitoso:', response.data);
		Swal.fire({
			icon: 'success',
			title: '¡Registro exitoso!',
			text: 'Te has registrado correctamente.',
		});
		// add authentification state
		router.push('/');

	} catch (error) {
		console.error('Error al registrar usuario', error);
		//errorMessage.value.general = 'Error al registrar el usuario. Inténtalo de nuevo.';
		Swal.fire({
			icon: 'error',
			title: 'Error',
			text: 'Hubo un error al registrar el usuario. Inténtalo de nuevo.',
		});
	} finally {
		sent.value = false; // Rehabilitamos el botón después de la petición
		console.log('Proceso de registro terminado.');
	}
};
</script>

<template>
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
