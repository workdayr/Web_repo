<script setup>
import { ref, onMounted } from "vue";
import HeaderComponent from "../HeaderComponent.vue";
import StatscardComponent from "../StatscardComponent.vue";
import GraphTemplate from "@/components/UI/GraphTemplate.vue";
const charts = ref([]);

const fetchChartData = async () => {
    try {
        const response = await fetch("https://backend-api/path");
        const data = await response.json();

        charts.value = [
            {
                id: 1,
                type: "line",
                data: {
                    labels: data.months,
                    datasets: [
                        {
                            label: "Active Users",
                            data: data.activeUsers,
                            borderColor: "#007bff",
                            backgroundColor: "rgba(0, 123, 255, 0.2)"
                        }
                    ]
                },
                options: { responsive: true }
            },
            {
                id: 2,
                type: "bar",
                data: {
                    labels: data.months,
                    datasets: [
                        {
                            label: "New Signups",
                            data: data.newUsers,
                            backgroundColor: "#28a745"
                        }
                    ]
                },
                options: { responsive: true }
            },
            {
                id: 3,
                type: "bar",
                data: {
                    labels: data.months,
                    datasets: [
                        {
                            label: "New Signups",
                            data: data.newUsers,
                            backgroundColor: "#28a745"
                        }
                    ]
                },
                options: { responsive: true }
            }
        ];
    } catch (error) {
        console.error("Error fetching chart data:", error);
    }
};

onMounted(fetchChartData);
</script>

<template>
    <div class="Section__content">
        <HeaderComponent text="User Analytics" />
        <div class="Section__StatCards">
            <StatscardComponent header="Recent Pageviews" amount="30K" />
            <StatscardComponent header="Recent Pageviews" amount="30K" />
            <StatscardComponent header="Recent Pageviews" amount="30K" />
            <StatscardComponent header="Recent Pageviews" amount="30K" />
        </div>
        <div class="Section__Graphs">
            <h6 class="Section__Graphs--header">Total Users</h6>
            <div class="row">
                <div class="col-md-6" v-for="chart in charts" :key="chart.id">
                    <GraphTemplate :chartType="chart.type" :chartData="chart.data" :chartOptions="chart.options" />
                </div>
            </div>
        </div>
    </div>
</template>
<style scoped>
@import "@/assets/styles/Dashboard/Sections/UseranalyticsSection.css";
</style>