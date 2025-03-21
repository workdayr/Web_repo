import axios from "axios";
//import { router } from 'vue-router';
import { useAuth } from "@/composables/useAuth";
import { authAPI } from "@/api/auth";

const api = axios.create({
    baseURL: "http://127.0.0.1:8000/api", 
    headers: {
        "Content-Type": "application/json",
    },
    timeout: 10000,
    withCredentials: true,
});

// Response Interceptor
api.interceptors.response.use(
    (response) => {
        return response;
    },
    async (error) => {
        if (error.response) {
            console.error('Response Error:', error.response.data);
            console.error('Status Code:', error.response.status);

            // Check for 401 error (Unauthorized)
            if (error.response.status === 401 && error.config && !error.config._retry) {
                error.config._retry = true;

                // Skip refresh if the request was already for the refresh token
                if (error.config.url === "/api/refresh-token") {
                    return Promise.reject(error);
                }

                try {
                    await authAPI.tokenRefresh();
                    // Retry the original request with the new token
                    return api(error.config);
                } catch (refreshError) {
                    console.error('Refresh token failed:', refreshError);

                    // If refresh token request fails, logout the user
                    useAuth().logout();
                    //router.push('/login');
                }
            } 
        } else {
            console.error('Network or server error:', error);
        }

        return Promise.reject(error);
    }
);

export default api;
