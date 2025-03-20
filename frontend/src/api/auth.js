import api from "./axios";

export const authAPI = {
  login: (email, password) => api.post("/login/", { email, password }),
  register: (userData) => api.post("/users/", userData),
  logout: () => api.post("/logout"),
  tokenRefresh: () => api.post("/token-refresh/"),
};  