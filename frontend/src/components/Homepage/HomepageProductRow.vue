<script setup>
import { defineProps, ref , onMounted} from 'vue';
import ProductPreview from '@/components/Common/ProductPreview.vue';

defineProps({
    products: {
        type: Array,
        required: true
    }
});
const sliderWrapper = ref(null);
let scrollAmount= 0;

onMounted(() => {
  if (sliderWrapper.value) {
    const computedStyle = window.getComputedStyle(sliderWrapper.value);
    const children = sliderWrapper.value.children;
    const gap = computedStyle.gap;
    const gapValue = parseFloat(gap);    
    scrollAmount = gapValue+Array.from(children)[0].getBoundingClientRect().width;
  }
});

const scrollPrev = () => {
    if (sliderWrapper.value) {
        sliderWrapper.value.scrollBy({ left: -scrollAmount, behavior: 'smooth' });
    }
};

const scrollNext = () => {
    if (sliderWrapper.value) {
        sliderWrapper.value.scrollBy({ left: scrollAmount, behavior: 'smooth' });
    }
};
</script>

<template>
    <div class="product__row">
        <button class="nav-button prev" @click="scrollPrev"><img src="@/assets/Common/Back.svg" alt=""></button>
        <button class="nav-button next" @click="scrollNext"><img src="@/assets/Common/Back.svg" alt=""></button>

        <div class="slider-wrapper" ref="sliderWrapper">
            <ProductPreview v-for="product in products" :key="product.id" :product="product" />
        </div>
    </div>
</template>

<style scoped>
@import "@/assets/styles/Homepage/HomepageProductRow.css";
</style>
