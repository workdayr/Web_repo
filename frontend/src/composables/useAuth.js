import { authAPI } from '@/api/auth';
import { useAuthStore } from '@/store/useAuthStore';

export function useAuth() {
    const authStore = useAuthStore();

    const login = async (credentials) => {
        try {
            const response = await authAPI.login(credentials);
            console.log(response.data.user);
            authStore.login(response.data);

            return response.data;
        } catch (error) {
            console.error("Login error:", error);
            throw error;
        }
    };

    const register = async (userData) => {
        try {
            //const hashedPassword = hashPassword(userData.password);
            //userData.password = hashedPassword;
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

        } catch (error) {
            console.error("Logout error:", error);
            throw error;
        }
    };

    const restoreSession = async () => {
        try {
            const response = await authAPI.tokenRefresh();

            //authStore.login(response.data.user);
            
            return response.data;
        } catch (error) {
            console.error("Restore session error:", error);
            return null;
        }
    };

    return {login, register, logout, restoreSession};
}

