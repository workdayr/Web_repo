
  <template>
    <div id="carouselExample" class="carousel slide" data-bs-ride="carousel" data-bs-interval="5000">
      <div class="carousel-inner">
        <div class="carousel-item active">
          <div class="gradient-placeholder-purple"></div>
        </div>
        <div class="carousel-item">
          <div class="gradient-placeholder-LightPurple"></div>
        </div>
        <div class="carousel-item">
          <div class="gradient-placeholder-gray"></div>
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
    height: 820px; /* Fijar la altura */
    object-fit: cover; /* Evita que la imagen se deforme */
  }
  </style>
  
  