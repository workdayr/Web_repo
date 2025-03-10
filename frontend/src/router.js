import { createRouter, createWebHistory } from "vue-router";
import HelloWorld from "@/views/HomepageView.vue"; // Index page
import LoginView from "@/views/LoginView.vue";
import FindBestPrices from "@/components/FindBestPrices.vue";
import OpinionsComponent from "@/components/OpinionsComponent.vue";
import ProductsComponent from "@/components/ProductsComponent.vue";
import RegisterComponent from "@/views/RegisterView.vue";
import DashboardView from "./views/DashboardView.vue";

const routes = [
  { path: "/", component: HelloWorld }, // Default page
  { path: "/login", component: LoginView},
  { path: "/find-best-prices", component: FindBestPrices },
  { path: "/opinions", component: OpinionsComponent },
  { path: "/products", component: ProductsComponent },
  { path: "/Register", component: RegisterComponent},
  {path: "/Dashboard", component: DashboardView},
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;

