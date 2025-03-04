<script setup>
import {ref, computed} from 'vue';
import RegisterInput from '@/components/RegisterInput.vue';

const states = ['asaaaaaaaaaaaaaaaaaaaa', 'b', 'c', 'd'];

const form = ref({
  fullName: '',
  email: '',
  password: '',
  confirmPassword: '',
  birthday: '',
  state: ''
});

const submitted = ref(false);

const regex = {
    fullName: /^[a-zA-Z\s]{3,50}$/,
    email: /^[^\s@]+@[^\s@]+\.[^\s@]+$/,
    password: /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/,
    confirmPassword: /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/,
}

const errorMessage = {
	fullName: "Name must be 3-50 letters",
	email: "Invalid email format",
	password: "Password must be at least 8 characters, including a number",
	confirmPassword: "Passwords do not match",
	birthday: "Invalid date",
	state: "Select at least one"
};

const minDate = new Date();
minDate.setFullYear(minDate.getFullYear() - 100);

const maxDate = new Date();
maxDate.setFullYear(maxDate.getFullYear() - 10); 

const validFields = computed(() => {
  if (!form.value) return {};
  
  return Object.keys(form.value).reduce((acc, key) => {
    if (key === "confirmPassword") {
      acc[key] = form.value[key] === form.value.password && regex[key] ? regex[key].test(form.value[key] || '') : false;
    } else if (key === "state") {
      acc[key] = !!form.value[key];
    } else if (key === "birthday") {
      const birthDate = new Date(form.value[key]);
      acc[key] = birthDate >= minDate && birthDate <= maxDate;
    }  
    else {
      acc[key] = regex[key] ? regex[key].test(form.value[key] || '') : true;
    }
    return acc;
  }, {});
});

const sent = ref(false);

const submitForm = async () =>{
    submitted.value = true;
    let isValid = Object.values(validFields.value).every(Boolean);
    if(isValid){
		sent.value = true;
		// POST LOGIC
	}
};
</script>

<template>
    
    <div class="register__background">
        <img class="background__shape1" src="@/assets/svg/Vector.svg" alt="Vector">
        <img class="background__shape2" src="@/assets/svg/backgroundShape.svg" alt="Background Shape">
    </div>
    
    <div class="register__container">
        <div class="register__header">
            <img class="back-arrow" src="@/assets/Register_icons/Back.svg" @click="$router.go(-1)">
            <h1 class="register__title">Register</h1>
        </div>
        <form class="register__form" @submit.prevent="submitForm">
            
            <RegisterInput v-model="form.fullName" :src="require('@/assets/Register_icons/Full_name.svg')" placeholder="Full Name" :is-valid="validFields['fullName']" :submitted="submitted" :error-message="errorMessage['fullName']"/>
            <RegisterInput v-model="form.email" :src="require('@/assets/Register_icons/Email.svg')" placeholder="Email" type="email" :is-valid="validFields['email']" :submitted="submitted" :error-message="errorMessage['email']"/>
            <RegisterInput v-model="form.password" :src="require('@/assets/Register_icons/Password.svg')" placeholder="Password" type="password" :is-valid="validFields['password']" :submitted="submitted" :error-message="errorMessage['password']"/>
            <RegisterInput v-model="form.confirmPassword" :src="require('@/assets/Register_icons/Password.svg')" placeholder="Confirm Password" type="password" :is-valid="validFields['confirmPassword']" :submitted="submitted" :error-message="errorMessage['confirmPassword']"/>
    
            
            <div class="register__row">
                <RegisterInput v-model="form.birthday" :src="require('@/assets/Register_icons/Birthday.svg')" placeholder="Birthday" type="date" :is-valid="validFields['birthday']" :submitted="submitted" :error-message="errorMessage['birthday']"/>
                <RegisterInput v-model="form.state" :src="require('@/assets/Register_icons/State.svg')" placeholder="State" type="select" :options="states" :is-valid="validFields['state']" :submitted="submitted" :error-message="errorMessage['state']"/>
            </div>
            <div class="register__button-container">
                <button type="submit" class="register__button">
					<span v-if="!sent">Create account</span> 
					<span class="loader" v-else></span>
                </button>
            </div>
        </form>
        
        <p class="register__text">
            By clicking "Create account" you agree to our 
            <a href="/terms" class="register__link">terms</a> and 
            <a href="/privacy-policy" class="register__link">privacy policy</a>.
        </p>

        
    </div>
</template>

<style scoped>
@import "@/assets/styles/RegisterComponent.css";
</style>
