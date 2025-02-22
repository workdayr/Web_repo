import { createRouter, createWebHistory } from "vue-router";
import HelloWorld from "@/components/HelloWorld.vue"; // Index page
import LoginComponent from "@/components/LoginComponent.vue";
import FindBestPrices from "@/components/FindBestPrices.vue";
import OpinionsComponent from "@/components/OpinionsComponent.vue";
import ProductsComponent from "@/components/ProductsComponent.vue";

const routes = [
  { path: "/", component: HelloWorld }, // Default page
  { path: "/login", component: LoginComponent },
  { path: "/find-best-prices", component: FindBestPrices },
  { path: "/opinions", component: OpinionsComponent },
  { path: "/products", component: ProductsComponent },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;

