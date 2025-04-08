import api from "./axios";

export const homepageService = {
  getSections: (sectionIndex) => api.get(`/homepage-sections/?section_index=${sectionIndex}`),
};  