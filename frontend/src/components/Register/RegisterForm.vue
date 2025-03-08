<script setup>
import {ref} from 'vue';
import AppInput from '@/components/Form/FormInput.vue';
import AppSubmitButton from '@/components/Form/FormSubmitButton.vue';
import { useRegisterValidation } from '@/composables/useRegisterValidation';

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

const submitForm = async () => {
  submitted.value = true;
  let isValid = Object.values(validFields.value).every(Boolean);
  if (isValid) {
    sent.value = true;
    // POST LOGIC
  }
};
</script>

<template>
	<form class="register__form" @submit.prevent="submitForm">
		
		<AppInput v-model="form.fullName" :src="require('@/assets/Form/Full_name.svg')" placeholder="Full Name" :is-valid="validFields['fullName']" :submitted="submitted" :error-message="errorMessage['fullName']"/>
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

