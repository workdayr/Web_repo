import { createApp } from 'vue'
import App from './App.vue'
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min.js';
import './assets/styles/Layout/NavbarComponent.css';
import './assets/styles/Layout/CarouselComponent.css';
import router from "./router"; // Import the router
import pinia from './store';


const app = createApp(App);
app.use(router); // Use the router
app.use(pinia);
app.mount("#app");
