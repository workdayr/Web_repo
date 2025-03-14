import { computed } from 'vue';

export function useRegisterValidation(form) {
  const errorMessage = computed(() => ({
    fullName: form.value.fullName.length >= 2 ? '' : 'El nombre debe tener al menos 2 caracteres.',
    email: /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(form.value.email) ? '' : 'Correo electrónico inválido.',
    password: /^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/.test(form.value.password) 
      ? '' 
      : 'La contraseña debe tener al menos 8 caracteres, una letra, un número y un carácter especial.',
    confirmPassword: form.value.password === form.value.confirmPassword 
      ? '' 
      : 'Las contraseñas no coinciden.',
    birthday: form.value.birthday && new Date().getFullYear() - new Date(form.value.birthday).getFullYear() >= 13
      ? '' 
      : 'Debes tener al menos 13 años.',
    state: form.value.state ? '' : 'Debes seleccionar un estado.',
  }));

  const validFields = computed(() => {
    return Object.keys(errorMessage.value).reduce((acc, field) => {
      return { ...acc, [field]: errorMessage.value[field] === '' };
    }, {});
  });

  return { validFields, errorMessage };
}
