<template>
  <div class="chart-container" :style="customStyles">
    
    <h5 class="chart-title">{{ chartHeader }}</h5>
    <p class="chart-subtitle">{{ chartSubtitle }}</p>

    <component :is="chartComponent" :data="chartData" :options="chartOptions" />
  </div>
</template>

<script setup>
import { defineProps, computed } from "vue";
import { Line, Bar, Pie, Doughnut } from "vue-chartjs";
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  LineElement,
  BarElement,
  ArcElement,
  PointElement,
  LinearScale,
  CategoryScale
} from "chart.js";

// Registrar los módulos de Chart.js
ChartJS.register(Title, Tooltip, Legend, LineElement, BarElement, ArcElement, PointElement, LinearScale, CategoryScale);

// Definir las props
const props = defineProps({
  chartHeader: String,
  chartSubtitle: String,
  chartType: String, // Tipo de gráfico ('line', 'bar', 'pie', etc.)
  chartData: Object, // Datos del backend
  chartOptions: Object, // Opciones de configuración
  customStyles: Object,
});

// Mapeo dinámico del tipo de gráfico
const chartComponent = computed(() => {
  const components = { line: Line, bar: Bar, pie: Pie, doughnut: Doughnut };
  return components[props.chartType] || Line;
});
</script>

<style scoped>
.chart-container {
  height: 100%;
  max-height: 500px;
  padding-bottom: 20%;
}

.chart__header--container{
  display: flex;
  flex-direction: column;
  justify-content: left;
}
.chart-title {
  font-size: small;
  text-align: left;
  color:#321647;
  margin-bottom: 10px;
}

.chart-subtitle {
  font-size: 1.2rem;
  font-weight:600;
  color: #321647;
  margin-bottom: 15px;
}
</style>