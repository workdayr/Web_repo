<template>
    <div class="chart-container">
        <h5 class="chart-title">{{ chartHeader }}</h5>
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
    chartType: String, // Tipo de gráfico ('line', 'bar', 'pie', etc.)
    chartData: Object, // Datos del backend
    chartOptions: Object // Opciones de configuración
  });
  
  // Mapeo dinámico del tipo de gráfico
  const chartComponent = computed(() => {
    const components = { line: Line, bar: Bar, pie: Pie, doughnut: Doughnut };
    return components[props.chartType] || Line;
  });
  </script>
  
  <style scoped>
  .chart-container {
    width: 100%;
    height: 300px;
  }

  .chart-title{
    font-size: large;
    color: black;
  }


  </style>
  