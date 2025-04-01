import { createRouter, createWebHistory } from "vue-router";
import HelloWorld from "@/views/HomepageView.vue"; // Index page
import LoginView from "@/views/LoginView.vue";
import FindBestPrices from "@/components/Homepage/FindBestPrices.vue";
import OpinionsComponent from "@/components/Homepage/OpinionsComponent.vue";
import RegisterComponent from "@/views/RegisterView.vue";
import DashboardView from "./views/DashboardView.vue";
import FaqView from "@/views/FaqView.vue";
import ProductView from '@/views/ProductView.vue';


const routes = [
  { path: "/", component: HelloWorld }, // Default page
  { path: "/login", component: LoginView},
  { path: "/find-best-prices", component: FindBestPrices },
  { path: "/opinions", component: OpinionsComponent },
  { path: "/Register", component: RegisterComponent},
  {path: "/Dashboard", component: DashboardView},
  {path: '/faq',component: FaqView},
  {path: '/product', component: ProductView},
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;

