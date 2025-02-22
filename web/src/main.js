import { createApp } from 'vue'
import App from './App.vue'
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min.js';
import './assets/styles/NavbarComponent.css';
import './assets/styles/CarouselComponent.css';
import router from "./router"; // Import the router

const app = createApp(App);
app.use(router); // Use the router
app.mount("#app");
