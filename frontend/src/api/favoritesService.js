import api from "./axios";

export const favoritesService = {
  getFavorites: (params) => api.get(`/favorites/`,{params}),
  addFavorites: (product_id) => api.post("/favorites/", {product_id}),
  removeFavorites: (favorite_id) => api.delete(`/favorites/${favorite_id}/`),
  removeFavoritesByProductId: (productId) => api.delete(`/favorites/remove-by-product/?product_id=${productId}`),
  patchFavorites: (favorite_id,data) => api.patch(`/favorites/${favorite_id}/`,data),
  
};  