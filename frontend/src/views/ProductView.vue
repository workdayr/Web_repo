<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue';
import { useRoute } from 'vue-router';
import NavBarComponent from '@/components/Layout/NavbarComponent.vue';
import ProductDetails from '@/components/Product/ProductDetails.vue';
import ProducPriceGraph from '@/components/Product/ProducPriceGraph.vue';
import PriceCard from '@/components/UI/PriceCard.vue';
import FooterComponent from '@/components/Layout/FooterComponent.vue';

const screenWidth = ref(window.innerWidth);
const productData = ref(null);
const route = useRoute();
const productId = ref(route.params.productId);

const updateScreenWidth = () => {
	screenWidth.value = window.innerWidth;
};
onMounted(() => {
	window.addEventListener('resize', updateScreenWidth);
});
onBeforeUnmount(() => {
	window.removeEventListener('resize', updateScreenWidth);
});

</script>

<template>
	<div class="product-view">
		<NavBarComponent />
		<ProductDetails :product_id="productId" :screen-width="screenWidth" />
		<ProducPriceGraph :product_id="productId" :screen-width="screenWidth"/>

		<div class="price-comparison">
			<PriceCard
				v-for="(offer, index) in productData?.prices || [{ price: 'Cargando...', store: 'Cargando...', features: 'Cargando...' }]"
				:key="index" :store="offer.store" :price="offer.price" :features="offer.features" />
		</div>

	</div>
	<FooterComponent />
</template>

<style scoped>
@import "@/assets/styles/Views/ProductView.css";
</style>