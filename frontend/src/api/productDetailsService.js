import api from "./axios";

export const productDetailsService = {
  getProduct: (product_id) => api.get(`/product_details/?product_id=${product_id}`),
};