<script>
import NavBarComponent from '@/components/Layout/NavbarComponent.vue';
import FooterComponent from '@/components/Layout/FooterComponent.vue';
import PriceCard from '@/components/UI/PriceCard.vue';
import AddFavoriteButton from '@/components/Common/AddFavoriteButton.vue';

export default {
  components: {
    NavBarComponent,
    PriceCard,
    FooterComponent,
    AddFavoriteButton
  },
  data() {
    return {
      isDescriptionExpanded: false,
      productData: null,
      loading: true,
      error: null,
      selectedImage: "https://picsum.photos/451/432", // Imagen principal por defecto
      thumbnails: [
        "https://picsum.photos/451/432?random=1",
        "https://picsum.photos/451/432?random=2",
        "https://picsum.photos/451/432?random=3"
      ]
    };
  },
  methods: {
    toggleDescription() {
      this.isDescriptionExpanded = !this.isDescriptionExpanded;
    },
    changeImage(newImage) {
      this.selectedImage = newImage;
    },
    async fetchProductData() {
      try {
        const response = await fetch('/api/producto?id=123');
        if (!response.ok) throw new Error('Error al cargar datos');
        this.productData = await response.json();
      } catch (err) {
        this.error = err.message;
      } finally {
        this.loading = false;
      }
    }
  },
  created() {
    this.fetchProductData();
  }
}
</script>

<template>
  <div class="product-view">
    <NavBarComponent />
    
    <div class="first-half">
      <div class="product-section">
        
        <img 
          :src="selectedImage" 
          alt="Product Image" 
          class="product-image"
        >
      
        <div class="thumbnail-container">
          <img 
            v-for="(thumb, index) in thumbnails" 
            :key="index"
            :src="thumb"  
            alt="Thumbnail"
            class="thumbnail-image"
            @click="changeImage(thumb)"
          >
        </div>  
      </div>
      <div class="product-details">
        <h2 class="product-title">LG 34GPT63A-B UltraWide Gaming Monitor 34" VA WQHD 160Hz 1ms MBR AMD FreeSync Premium, HDMI, Display Port, Curvo 1800R</h2>
        <p class="price-label">Lowest price:</p>
        <p class="product-price">$9,999.99 MXN</p>
        <p class="store-product">on amazon</p>
 <!-- Descripción con efecto click-to-expand -->
          <div class="description-container">
          <p 
            class="description-text" 
            :class="{ 'collapsed': !isDescriptionExpanded, 'expanded': isDescriptionExpanded }"
            @click="toggleDescription"
          >
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent porttitor efficitur mauris, a vehicula mi congue non. Aenean a viverra mauris. Pellentesque nulla dui, consequat et leo sit amet, placerat volutpat mi. Phasellus id urna quis erat commodo ultricies ut eu tortor. Morbi sapien risus, maximus eu diam eu, ultrices dapibus lacus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas elit dolor, lobortis ut lacinia eu, rhoncus quis magna. Aliquam et orci quis nunc placerat gravida.
          </p>
          </div>

        <div class="favorite-button-container">
        <AddFavoriteButton />
        <p class="follow-text">Follow product</p>
        </div>
      </div>
    </div>

    <div class="dynamic-table-section">
      <!-- Aquí irá el contenido de la tabla dinámica -->
    </div>

    <div class="price-comparison">
      <PriceCard
        store="Amazon"
        :price="0"
        :features="['Envio gratis o con tarifas de importación', 'Metodos de pago: Tarjeta, Efectivo (tiendas participantes), Kueski Pay', 'Cuenta de Amazon requerida']"
      />
      <PriceCard
        store="Mercado Libre"
        :price="0"
        :features="['Costo de envio depende del producto/vendedor', 'Metodos de pago: Tarjeta, Efectivo (tiendas participantes), Mercado pago, Depositos y transferencias bancarias', 'Cuenta de Mercado libre requerida']"
      />
      <PriceCard
        store="Walmart"
        :price="0"
        :features="['Envio gratis', 'Metodos de pago: Tarjeta, Cashi, PayPal, pagar en tienda', 'Cuenta de Walmart requerida']"
      />
    </div>

    <FooterComponent />
  </div>
</template>
  

  
  <style scoped>
  @import "@/assets/styles/Product/ProductView.css";

  .product-title {
  color: white;
  font-size: 27px;
  font-weight: bold;
  margin-bottom: 10px; /* Esto creará espacio entre el título y price-label */
  position: relative;
  top: -120px; /* Esto subirá el título de su posición actual */
}
  </style>
  