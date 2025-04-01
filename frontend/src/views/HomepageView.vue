<template>
  <section id="Homepage">
    <NavbarComponent :is-always-compact="false"/>

    <CarouselComponent :slides="carouselSlides"/>

  <div class="hompage-content">
    <FindBestPrices/>
    <HomepageSection v-for="section in sections" class="homepage-section" :key="section.id" :title="section.title" :icon="section.icon" :products="section.products"/>
    <!-- <OpinionsComponent />-->
    
  </div>
  <FooterComponent/>

  </section>
</template>

<script setup>
import NavbarComponent from '@/components/Layout/NavbarComponent.vue';
import CarouselComponent from '@/components/Layout/CarouselComponent.vue'; 
import FindBestPrices from '@/components/Homepage/FindBestPrices.vue';
import HomepageSection from '@/components/Homepage/HomepageSection.vue';
import FooterComponent from '@/components/Layout/FooterComponent.vue';
//import OpinionsComponent from '@/components/Homepage/OpinionsComponent.vue';



/*
  EXAMPLE DATA FETCH RESULT
*/
const exampleProducts = [
{
    "product_id": 1,
    "brand": 1,
    "current_lowest_price": null,
    "name": "product1",
    "upc": "1",
    "description": "some description"
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
  },];

  const carouselSlides = [
  {
    "text": "Compare prices across \ndifferent websites",
    "gradient": "linear-gradient(to bottom, #4D1270, #561960)",
    "icon": require("@/assets/Carrusel_icons/Slide1.svg"),
    "textPosition": "center-left",
    "iconPosition": "center-right"
  },
  {
    "text": "Track product prices \nover time",
    "gradient": "linear-gradient(to bottom, #562F7F, #835EAB)",
    "icon": require("@/assets/Carrusel_icons/Slide1.svg"),
    "textPosition": "center-right",
    "iconPosition": "center-left"
  },
  {
    "text": "Stay Signed In For Notifications on \nPrice Changes",
    "gradient": "linear-gradient(to bottom, #4D1270, #feb47b)",
    "icon": "",//require("@/assets/Carrusel_icons/Slide1.svg"),
    "textPosition": "center",
    "iconPosition": "center-right"
  },
]

const sections = [{"id":0, "title": "Best Sales", "icon": require("@/assets/Layout/Footer/instagram-icon.png"),"products": exampleProducts},{"id":1,"title": "You may also like", "products": exampleProducts}]
</script>

<style scoped>
@import "@/assets/styles/Views/HomepageView.css";
</style>
