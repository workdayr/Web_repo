<template>
  <div id="carouselExample" class="carousel slide" data-bs-ride="carousel" data-bs-interval="5000">
    <div class="carousel-inner">
      <div 
        v-for="(slide, index) in slides" 
        :key="index" 
        class="carousel-item" 
        :class="{ active: index === 0 }"
      >
        <div :class="slide.gradientClass">
          <!-- Usamos v-html para procesar los saltos de línea -->
          <p :class="['carousel-text', 'text-slide-' + (index + 1)]" v-html="formatText(slide.text)"></p>
        </div>
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
  data() {
    return {
      slides: [
        { text: 'Compara precios entre \n diferentes sitios', gradientClass: 'gradient-placeholder-purple' },
        { text: 'Sigue el precio de los productos\na través del tiempo', gradientClass: 'gradient-placeholder-LightPurple' },
        { text: 'BPRCS\n\n\nMantén tu sesión activa para ser notificado\nen el cambio de precio', gradientClass: 'gradient-placeholder-gray' },
      ]
    }
  },
  methods: {
    // Método para convertir los saltos de línea en <br>
    formatText(text) {
      return text.replace(/\n/g, '<br>'); // Reemplaza \n con <br>
    }
  }
}
</script>

<style scoped>
@import "@/assets/styles/CarouselComponent.css"; /* Importa el archivo de estilos */
</style>
