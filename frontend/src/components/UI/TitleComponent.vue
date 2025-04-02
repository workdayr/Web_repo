<template>
    <div class="title-container">
      <h1 :class="sizeClass">{{ text }}</h1>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      text: {
        type: String,
        required: true
      },
      size: {
        type: String,
        default: "large", // Puede ser "small", "medium" o "large"
      }
    },
    computed: {
      sizeClass() {
        return {
          "text-lg": this.size === "large",
          "text-md": this.size === "medium",
          "text-sm": this.size === "small",
        };
      }
    }
  };
  </script>
  
  <style scoped>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;700&display=swap');
  @import "@/assets/styles/UI/TitleComponent.css";
  </style>
  