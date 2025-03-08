import {computed } from 'vue';

export function useRegisterValidation(form) {
  const regex = {
    fullName: /^[a-zA-Z\s]{3,50}$/,
    email: /^[^\s@]+@[^\s@]+\.[^\s@]+$/,
    password: /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/,
    confirmPassword: /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/,
    username: /^.{3,}$/,
    passwordLogin:/^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/,
  };

  const errorMessage = {
    fullName: "Name must be 3-50 letters",
    email: "Invalid email format",
    password: "Password must be at least 8 characters, including a number",
    confirmPassword: "Passwords do not match",
    birthday: "Invalid date",
    state: "Select at least one",
    username: "Username is required",
    passwordLogin: "Password is required",
  };

  const minDate = new Date();
  minDate.setFullYear(minDate.getFullYear() - 100);
  const maxDate = new Date();
  maxDate.setFullYear(minDate.getFullYear() - 10);

  const validFields = computed(() => {
    return Object.keys(form.value).reduce((acc, key) => {
      if (key === "confirmPassword") {
        acc[key] = form.value[key] === form.value.password && regex[key].test(form.value[key] || '');
      } else if (key === "state") {
        acc[key] = !!form.value[key];
      } else if (key === "birthday") {
        const birthDate = new Date(form.value[key]);
        acc[key] = birthDate >= minDate && birthDate <= maxDate;
      } else {
        acc[key] = regex[key] ? regex[key].test(form.value[key] || '') : true;
      }
      return acc;
    }, {});
  });

  return { validFields, errorMessage };
}