import { defineStore } from 'pinia';
import { ref } from 'vue';
import { useRouter } from 'vue-router';

export const useAuthStore = defineStore('auth', () => {
  const user = ref(null);
  const isAuthenticated = ref(false);
  const router = useRouter();

  function login(newUser) {
    user.value = newUser;
    isAuthenticated.value = true;
  }

  function logout() {
    user.value = null;
    isAuthenticated.value = false;
  }

  function checkAuthorization() {
    if (!isAuthenticated.value) {
      router.push('/login');
      return false;
    }
    else return true;
  }

  return {
    user,
    isAuthenticated,
    login,
    logout,
    checkAuthorization, 
  };
});