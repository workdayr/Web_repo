<script>
  import TitleComponent from "@/components/UI/TitleComponent.vue";
  import FaqItemComponent from "@/components/UI/FaqItemComponent.vue";
  export default {
    components: {
      TitleComponent,
      FaqItemComponent,
    }
  };
  </script>

<template>
 
    <div class="background__vectors">
      <img v-for="n in 8" :key="n" 
           :src="require(`@/assets/FAQ_icons/Vector${n}.svg`)"
           :class="`background__vector${n}`" 
           :alt="`Vector ${n}`">
    </div>


    
      <!-- Título principal -->
      <TitleComponent text="Frequently Asked Questions" size="large" />
  
      <!-- Sección de preguntas frecuentes -->
        <FaqItemComponent
          question="What is BPrices and How It works?"
          answer="Answer here"
        />
        <FaqItemComponent
          question="On which online platforms does the web compare prices?"
          answer="Answer here."
        />
        <FaqItemComponent
          question="How often are prices updated?"
          answer="Answer here."
        />
        <FaqItemComponent
          question="Do I need an account to use the app?"
          answer="No, you can use the app without an account, but some features will require signing up."
        />

        <TitleComponent text="Use and Functionalities" size="large" />

        <FaqItemComponent
          question="How can I search for a specific product?"
          answer="Answer here"
        />
        <FaqItemComponent
          question="Can I receive alerts when a product's price drops?"
          answer="Answer here"
        />
        <FaqItemComponent
          question="Can I filter results by free shipping, delivery time, etc?"
          answer="Answer here."
        />
        <FaqItemComponent
          question="Can I receive alerts when a product's price drops?"
          answer="Answer here"
        />

        <TitleComponent text="Shopping and Security" size="large" />

        <FaqItemComponent
          question="Can I purchase directly from the app?"
          answer="Answer here"
        />
        <FaqItemComponent
          question="How do I know the pricces shown are accurate and reliable?"
          answer="Answer here."
        />
        <FaqItemComponent
          question="What do I do if I see a difference between the price in the app and the price on the reail website?"
          answer="Answer here."
        />

     
  </template>
  
  
  
  <style scoped>
@import "@/assets/styles/FAQ/FaqView.css"
  </style>
  