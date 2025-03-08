import { createRouter, createWebHistory } from "vue-router";
import HelloWorld from "@/views/HomepageView.vue"; // Index page
import LoginComponent from "@/components/LoginComponent.vue";
import FindBestPrices from "@/components/FindBestPrices.vue";
import OpinionsComponent from "@/components/OpinionsComponent.vue";
import ProductsComponent from "@/components/ProductsComponent.vue";
import RegisterComponent from "@/views/RegisterView.vue";

const routes = [
  { path: "/", component: HelloWorld }, // Default page
  { path: "/login", component: LoginComponent },
  { path: "/find-best-prices", component: FindBestPrices },
  { path: "/opinions", component: OpinionsComponent },
  { path: "/products", component: ProductsComponent },
  { path: "/Register", component: RegisterComponent},
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;

