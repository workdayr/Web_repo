<script setup>
import { ref } from 'vue';
import axios from 'axios';
import AppInput from '@/components/Form/FormInput.vue';
import AppSubmitButton from '@/components/Form/FormSubmitButton.vue';
import { useRegisterValidation } from '@/composables/useRegisterValidation';
import { hashPassword } from '@/utils/hashUtils'; // Asegúrate de crear esta función

const form = ref({
  fullName: '',
  email: '',
  password: '',
  confirmPassword: '',
  birthday: ''
});

const submitted = ref(false);
const sent = ref(false);
const errorMessage = ref({});

// Importar validaciones
const { validFields } = useRegisterValidation(form);

// URL del backend (ajústala según corresponda)
const API_URL = 'http://127.0.0.1:8000/users/';

// Función para manejar el envío del formulario
const submitForm = async () => {
  submitted.value = true;
  
  // Validamos los campos
  let isValid = Object.values(validFields.value).every(Boolean);
  if (!isValid) {
    return;
  }

  // Hashear la contraseña antes de enviarla
  const hashedPassword = await hashPassword(form.value.password);

  const payload = {
    username: form.value.email, // Se usa el email como username
    first_name: form.value.fullName.split(' ')[0], // Extraer primer nombre
    last_name: form.value.fullName.split(' ').slice(1).join(' ') || "", // Extraer el apellido si existe
    email: form.value.email,
    password: hashedPassword, // Se envía la contraseña en SHA-256 con sal
    date_of_birth: form.value.birthday
  };

  try {
    sent.value = true; // Bloqueamos el botón mientras se procesa la petición
    const response = await axios.post(API_URL, payload);
    console.log('Registro exitoso:', response.data);
    // Aquí podrías redirigir al usuario a otra página, por ejemplo:
    //router.push('/');
  } catch (error) {
    console.error('Error al registrar usuario', error);
    errorMessage.value.general = 'Error al registrar el usuario. Inténtalo de nuevo.';
  } finally {
    sent.value = false; // Rehabilitamos el botón después de la petición
  }
};
</script>


<template>
	<form class="register__form" @submit.prevent="submitForm">
		<AppInput v-model="form.fullName" :src="require('@/assets/Form/FullName.svg')" placeholder="Full Name" :is-valid="validFields['fullName']" :submitted="submitted" :error-message="errorMessage['fullName']"/>
		<AppInput v-model="form.email" :src="require('@/assets/Form/Email.svg')" placeholder="Email" type="email" :is-valid="validFields['email']" :submitted="submitted" :error-message="errorMessage['email']"/>
		<AppInput v-model="form.password" :src="require('@/assets/Form/Password.svg')" placeholder="Password" type="password" :is-valid="validFields['password']" :submitted="submitted" :error-message="errorMessage['password']"/>
		<AppInput v-model="form.confirmPassword" :src="require('@/assets/Form/Password.svg')" placeholder="Confirm Password" type="password" :is-valid="validFields['confirmPassword']" :submitted="submitted" :error-message="errorMessage['confirmPassword']"/>
		
		<div class="form__group">
			<AppInput v-model="form.birthday" :src="require('@/assets/Form/Birthday.svg')" placeholder="Birthday" type="date" :is-valid="validFields['birthday']" :submitted="submitted" :error-message="errorMessage['birthday']"/>
		</div>
		
		<AppSubmitButton :sent="sent"/>
	</form>
</template>


<style lang="css">
@import "@/assets/styles/Register/RegisterForm.css";
</style>