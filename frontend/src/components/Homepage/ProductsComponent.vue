<script setup>
import HomepageSection from '@/components/Homepage/HomepageSection.vue';
const exampleProducts = [
{
    'title': 'example product 1',
    'symbol': '$',
    'priceWhole': '9999',
    'priceFraction': '00',
    'imageUrl': ''
  },
  {
    'title': 'aaaaaaaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaaaaa',
    'symbol': '$',
    'priceWhole': '10',
    'priceFraction': '00',
    'imageUrl': ''
  },
  {
    'title': 'example product 1',
    'symbol': '$',
    'priceWhole': '9999',
    'priceFraction': '00',
    'imageUrl': ''
  },
  {
    'title': '',
    'symbol': '',
    'priceWhole': '',
    'priceFraction': '',
    'imageUrl': ''
  },
  {
    'title': 'example product 1',
    'symbol': '$',
    'priceWhole': '9999',
    'priceFraction': '00',
    'imageUrl': ''
  },
  {
    'title': '',
    'symbol': '',
    'priceWhole': '',
    'priceFraction': '',
    'imageUrl': ''
  },
  {
    'title': 'example product 1',
    'symbol': '$',
    'priceWhole': '9999',
    'priceFraction': '00',
    'imageUrl': ''
  },
  {
    'title': '',
    'symbol': '',
    'priceWhole': '',
    'priceFraction': '',
    'imageUrl': ''
  },
  {
    'title': 'example product 1',
    'symbol': '$',
    'priceWhole': '9999',
    'priceFraction': '00',
    'imageUrl': ''
  },
  {
    'title': '',
    'symbol': '',
    'priceWhole': '',
    'priceFraction': '',
    'imageUrl': ''
  },
  {
    'title': 'example product 1',
    'symbol': '$',
    'priceWhole': '9999',
    'priceFraction': '00',
    'imageUrl': ''
  },
  {
    'title': '',
    'symbol': '',
    'priceWhole': '',
    'priceFraction': '',
    'imageUrl': ''
  },
 

]
const sections = [{"id":0, "title": "Best Sales", "products": exampleProducts},{"id":1,"title": "You may also like", "products": exampleProducts}]
</script>

<template>
    <div class="hompage__section">
        <HomepageSection v-for="section in sections" :key="section.id" :title="section.title" :products="section.products"/>
    </div>
</template>


<style scoped>
@import "@/assets/styles/Homepage/ProductsComponent.css";
</style>