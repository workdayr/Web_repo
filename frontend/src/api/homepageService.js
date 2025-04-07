import api from "./axios";

export const homepageService = {
  getSections: () => api.get(`/homepage-sections/`),
};  