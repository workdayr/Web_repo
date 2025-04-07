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
      const originalRequest = error.config;
  
      // Always reject login and refresh errors immediately
      if (originalRequest?.url === "/login/" || originalRequest?.url === "/token-refresh/") {
        return Promise.reject(error); // Let login handle its own 401
      }
      if (error.response) {
        if (
          error.response.status === 401 &&
          originalRequest &&
          !originalRequest._retry
        ) {
          originalRequest._retry = true;
  
          if (!isRefreshing) {
            isRefreshing = true;
            refreshPromise = authAPI
              .tokenRefresh()
              .then(() => api(originalRequest))
              .catch(async (refreshError) => {
                try {
                  await useAuth().logout();
                } catch (logoutError) {
                  console.error("Logout error:", logoutError);
                } finally {
                  router.push("/login");
                }
                return Promise.reject(refreshError);
              })
              .finally(() => {
                isRefreshing = false;
                refreshPromise = null;
              });
          }
  
          return refreshPromise;
        }
      } else {
        console.error("Network or server error:", error);
      }
  
      return Promise.reject(error);
    }
  );
  
  


export default api;
