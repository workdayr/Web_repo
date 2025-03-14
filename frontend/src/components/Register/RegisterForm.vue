<script setup>
import { ref } from 'vue';
import axios from 'axios';
import AppInput from '@/components/Form/FormInput.vue';
import AppSubmitButton from '@/components/Form/FormSubmitButton.vue';
import { useRegisterValidation } from '@/composables/useRegisterValidation';
import { hashPassword } from '@/utils/hashUtils'; // Asegúrate de tener esta función
import Swal from 'sweetalert2'; // Importa SweetAlert2

const states = ['State A', 'State B', 'State C']; // Mantén la lista de estados

const form = ref({
  fullName: '',
  email: '',
  password: '',
  confirmPassword: '',
  birthday: '',
  state: '' // Campo del estado añadido
});

const submitted = ref(false);
const sent = ref(false);
const errorMessage = ref({});

const { validFields } = useRegisterValidation(form);

// URL del backend (ajústala según corresponda)
const API_URL = 'http://127.0.0.1:8000/api/users/';

// Función para manejar el envío del formulario
const submitForm = async () => {
  submitted.value = true;

  // Verificar si los campos son válidos
  let isValid = Object.values(validFields.value).every(Boolean);
  if (!isValid) {
    Swal.fire({
      icon: 'error',
      title: 'Formulario no válido',
      text: 'Asegúrate de llenar todos los campos correctamente.',
    });
    console.log('Formulario no válido:', validFields.value);
    return;
  }

  // Hashear la contraseña antes de enviarla
  const hashedPassword = await hashPassword(form.value.password);
  console.log('Contraseña hasheada:', hashedPassword);

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
    sent.value = true; // Bloqueamos el botón mientras se procesa la petición
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
    // Aquí podrías redirigir al usuario a otra página, por ejemplo:
    // router.push('/');

  } catch (error) {
    console.error('Error al registrar usuario', error);
    errorMessage.value.general = 'Error al registrar el usuario. Inténtalo de nuevo.';
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
    
    <AppInput v-model="form.fullName" :src="require('@/assets/Form/FullName.svg')" placeholder="Full Name" :is-valid="validFields['fullName']" :submitted="submitted" :error-message="errorMessage['fullName']"/>
    <AppInput v-model="form.email" :src="require('@/assets/Form/Email.svg')" placeholder="Email" type="email" :is-valid="validFields['email']" :submitted="submitted" :error-message="errorMessage['email']"/>
    <AppInput v-model="form.password" :src="require('@/assets/Form/Password.svg')" placeholder="Password" type="password" :is-valid="validFields['password']" :submitted="submitted" :error-message="errorMessage['password']"/>
    <AppInput v-model="form.confirmPassword" :src="require('@/assets/Form/Password.svg')" placeholder="Confirm Password" type="password" :is-valid="validFields['confirmPassword']" :submitted="submitted" :error-message="errorMessage['confirmPassword']"/>
    
    <div class="register__row">
      <AppInput v-model="form.birthday" :src="require('@/assets/Form/Birthday.svg')" placeholder="Birthday" type="date" :is-valid="validFields['birthday']" :submitted="submitted" :error-message="errorMessage['birthday']"/>
      <AppInput v-model="form.state" :src="require('@/assets/Form/State.svg')" placeholder="State" type="select" :options="states" :is-valid="validFields['state']" :submitted="submitted" :error-message="errorMessage['state']"/>
    </div>

    <AppSubmitButton text="Create account" :sent="sent"/>
  </form>
</template>

<style lang="css">
@import "@/assets/styles/Register/RegisterForm.css";
</style>
