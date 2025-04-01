import axios from "axios";
import router from "@/router";
import { useAuth } from "@/composables/useAuth";
import { authAPI } from "@/api/authService";

const api = axios.create({
    baseURL: "http://127.0.0.1:8000/api",
    headers: {
        "Content-Type": "application/json",
    },
    timeout: 10000,
    withCredentials: true,
});


let isRefreshing = false;
let refreshPromise = null;

// Response Interceptor
api.interceptors.response.use(
    (response) => response,
    async (error) => {
        if (error.response) {
            //console.error('Response Error:', error.response.data);
            //console.error('Status Code:', error.response.status);

            if (error.response.status === 401 && error.config && !error.config._retry) {
                error.config._retry = true;

                // Skip refresh if the request was already for the refresh token
                if (error.config.url === "/api/token-refresh") {
                    return Promise.reject(error);
                }

                if (!isRefreshing) {
                    isRefreshing = true;
                    console.log('promise executing');
                    refreshPromise = authAPI.tokenRefresh()
                        .then(() => api(error.config)) // Retry original request
                        .catch(async (refreshError) => {
                            try {
                                await useAuth().logout();
                            } catch (logoutError) {
                                console.error('Logout error:', logoutError);
                            } finally {
                                router.push('/login');
                            }
                            return Promise.reject(refreshError);
                        })
                        .finally(() => {
                            isRefreshing = false;
                            refreshPromise = null;
                        });
                }

                return refreshPromise.then(() => api(error.config));
            }
        } else {
            console.error('Network or server error:', error);
        }

        return Promise.reject(error);
    }
);


export default api;
