import api from "./axios";

export const authAPI = {
  login: (credentials) => api.post("/login/", credentials),
  register: (userData) => api.post("/users/", userData),
  logout: () => api.post("/logout"),
  tokenRefresh: () => api.post("/token-refresh/"),
};  