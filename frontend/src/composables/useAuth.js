import { authAPI } from '@/api/auth';
import { useAuthStore } from '@/store/useAuthStore';

export function useAuth() {
    const authStore = useAuthStore();

    const login = async (email, password) => {
        try {
            const response = await authAPI.login(email, password);
            authStore.login(response.data.user);

            return response.data;
        } catch (error) {
            console.error("Login error:", error);
            throw error;
        }
    };

    const register = async (userData) => {
        try {
            console.log("from register", userData);
            //const hashedPassword = hashPassword(userData.password);
            //userData.password = hashedPassword;
            const response = await authAPI.register(userData);
            await login(userData.email, userData.password);

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

            authStore.login(response.data.user);
            
            return response.data;
        } catch (error) {
            console.error("Restore session error:", error);
            return null;
        }
    };

    return {login, register, logout, restoreSession};
}

