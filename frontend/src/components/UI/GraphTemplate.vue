<template>
  <div class="chart-container" :style="containerStyles">
    <h5 class="chart-title">{{ chartHeader }}</h5>
    <p class="chart-subtitle">{{ chartSubtitle }}</p>
    <component
      v-if="chartComponent"
      :style="customStyles"
      :is="chartComponent"
      :data="chartData"
      :options="chartOptions"
    />
    <p v-else class="chart-error">Invalid chart type: {{ chartType }}</p>
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
  CategoryScale,
} from "chart.js";

// Register Chart.js modules
ChartJS.register(
  Title,
  Tooltip,
  Legend,
  LineElement,
  BarElement,
  ArcElement,
  PointElement,
  LinearScale,
  CategoryScale
);

// Define props
const props = defineProps({
  chartHeader: String,
  chartSubtitle: String,
  chartType: String,
  chartData: Object,
  chartOptions: Object,
  customStyles: Object, // Passed styles for dynamic control
});

// Dynamically determine which chart component to use
const chartComponent = computed(() => {
  const components = { line: Line, bar: Bar, pie: Pie, doughnut: Doughnut };
  return components[props.chartType] || Line;
});

// Use customStyles for the outer container as well
const containerStyles = computed(() => ({
  width: props.customStyles?.width || "100%",
  height: props.customStyles?.height || "500px", // Default height if none provided
  maxHeight: props.customStyles?.maxHeight || "500px",
  marginBottom: props.customStyles?.marginBottom || "12px"
}));
</script>

<style scoped>
.chart-container {
  width: 100%;
  position: relative;
  border-radius: 12px;
}

.chart-title {
  font-size: 1.1rem;
  text-align: left;
  margin-bottom: 8px;
  color: #321647;
}

.chart-subtitle {
  font-size: 0.9rem;
  font-weight: 500;
  color: #6c757d;
  margin-bottom: 12px;
}

.chart-error {
  color: red;
  font-size: 1rem;
}
</style>
