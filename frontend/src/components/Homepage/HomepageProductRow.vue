<script setup>
import { ref, onMounted, nextTick, defineProps } from 'vue'; // Añade defineProps aquí
import ProductPreview from '@/components/Common/ProductPreview.vue';

const props = defineProps({
    products: {
        type: Array,
        required: true,
        default: () => []
    }
});

const sliderWrapper = ref(null);
const scrollAmount = ref(300);

const scrollPrev = () => {
    if (sliderWrapper.value) {
        sliderWrapper.value.scrollBy({ left: -scrollAmount.value, behavior: 'smooth' });
    }
};

const scrollNext = () => {
    if (sliderWrapper.value) {
        sliderWrapper.value.scrollBy({ left: scrollAmount.value, behavior: 'smooth' });
    }
};

onMounted(async () => {
  await nextTick();
  
  if (sliderWrapper.value?.children?.length > 0) {
    const firstChild = sliderWrapper.value.children[0];
    if (firstChild) {
      const style = window.getComputedStyle(sliderWrapper.value);
      const gap = parseFloat(style.gap) || 0;
      scrollAmount.value = firstChild.getBoundingClientRect().width + gap;
    }
  }
});
</script>

<template>
    <div class="product__row">
        <button class="nav-button prev" @click="scrollPrev">
            <img src="@/assets/Common/Back.svg" alt="Previous">
        </button>
        
        <div class="slider-wrapper" ref="sliderWrapper">
            <ProductPreview 
                v-for="product in props.products" 
                :key="product.product_id || product.id" 
                :product="product" 
            />
        </div>
        
        <button class="nav-button next" @click="scrollNext">
            <img src="@/assets/Common/Back.svg" alt="Next">
        </button>
    </div>
</template>

<style scoped>
@import "@/assets/styles/Homepage/HomepageProductRow.css";
</style>