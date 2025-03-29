import { authAPI } from '@/api/authService';
import { useAuthStore } from '@/store/useAuthStore';

export function useAuth() {
    const authStore = useAuthStore();

    const login = async (credentials) => {
        try {
            if (authStore.isAuthenticated) {
                await logout();
            }

            const response = await authAPI.login(credentials);
        
            authStore.login(response.data.user);
        
            return response.data;
        } catch (error) {
            console.error("Login error:", error);
            throw error;
        }
    };

    const register = async (userData) => {
        try {
            const response = await authAPI.register(userData);
            const credentials = {email: userData.email, password: userData.password};
            await login(credentials);

            return response.data;
        } catch (error) {
            console.error("Register error:", error);
            throw error;
        }
    };

    const logout = async () => {
        try {
            await authAPI.logout();
            authStore.logout();
            window.location.reload();
        } catch (error) {
            console.error("Logout error:", error);
            throw error;
        }
    };

    const restoreSession = async () => {
        try {
            
            const response = await authAPI.restoreSession();
            
            authStore.login(response.data.user);
        
            return response.data;
        } catch (error) {
            console.error("Unable to restore session:", error.message);
            return null;
        }
    };

    return {login, register, logout, restoreSession};
}

