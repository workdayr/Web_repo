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
                header: "Total Users",
                type: "line",
                data: {
                    labels: data.months,
                    datasets: [
                        {
                            label: "Users",
                            data: data.totalUsers,
                            borderColor: "#007bff",
                            backgroundColor: "rgba(0, 123, 255, 0.2)"
                        }
                    ]
                },
                options: { responsive: true }
            },
            {
                id: 2,
                header: "Total views",
                type: "bar",
                data: {
                    labels: data.months,
                    datasets: [
                        {
                            label: "Views",
                            data: data.totalViews,
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
        <div class="Section__content--graphs">
        <div class="Section__content--graph1">
            <div class="row">
                <div class="col-md-6" v-for="chart in charts" :key="chart.id">
                    <GraphTemplate :chartHeader="chart.header" :chartType="chart.type" :chartData="chart.data" :chartOptions="chart.options" />
                </div>
            </div>
        </div>
    </div>
    </div>
</template>

<style scoped>
@import "@/assets/styles/Dashboard/Sections/UseranalyticsSection.css";
</style>