import { defineStore } from 'pinia';
import { ref, computed } from 'vue';

export const useAuthStore = defineStore('auth', () => {
  const user = ref(null);
  const isAuthenticated = ref(false);

  function login(newUser) {
    user.value = newUser;
    isAuthenticated.value = true;
  }

  function logout() {
    token.value = null;
    user.value = null;
    isAuthenticated.value = false;
  }

  return {
    user,
    isAuthenticated,
    login,
    logout,
  };
});