<template>
  <div id="carouselExample" class="carousel slide" data-bs-ride="carousel" data-bs-interval="5000">
    <div class="carousel-inner">
      <div class="carousel-item active">
        <img src="https://dummyimage.com/1920x420/000/fff&text=Slide+1" class="d-block w-100" alt="Placeholder">
      </div>
      <div class="carousel-item">
        <img src="https://dummyimage.com/1920x420/000/fff&text=Slide+2" class="d-block w-100" alt="Placeholder">
      </div>
      <div class="carousel-item">
        <img src="https://dummyimage.com/1920x420/000/fff&text=Slide+3" class="d-block w-100" alt="Placeholder">
      </div>
    </div>
    <button class="carousel-control-prev" type="button" data-bs-target="#carouselExample" data-bs-slide="prev">
      <span class="carousel-control-prev-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Previous</span>
    </button>
    <button class="carousel-control-next" type="button" data-bs-target="#carouselExample" data-bs-slide="next">
      <span class="carousel-control-next-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Next</span>
    </button>
  </div>
</template>

<script>
export default {
  name: 'CarouselComponent',
}
</script>

<style scoped>
@import "@/assets/styles/CarouselComponent.css"; /* Importa el archivo de estilos */

.carousel img {
  width: 100%;
  height: 420px; /* Fijar la altura */
  object-fit: cover; /* Evita que la imagen se deforme */
}
</style>
