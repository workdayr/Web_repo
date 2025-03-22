<script setup>
import { ref, onMounted } from "vue";
import HeaderComponent from "../HeaderComponent.vue";
import StatscardComponent from "../StatscardComponent.vue";
import GraphTemplate from "@/components/UI/GraphTemplate.vue";
import { fetchChartData } from "@/api/userChartService";

const charts = ref([]);
const stats = ref({});

const loadData = async () => {
    const { charts: chartData, stats: statsData } = await fetchChartData();
    charts.value = chartData;
    stats.value = statsData;
};

onMounted(loadData);
</script>

<template>
    <div class="Section__content">

        <HeaderComponent text="User Analytics" />

        <div class="Section__StatCards">
            <StatscardComponent header="Recent Pageviews"
                :amount="stats.totalPageviews ? stats.totalPageviews.toLocaleString() : '0'" />
            <StatscardComponent header="New Signups"
                :amount="stats.totalNewSignups ? stats.totalNewSignups.toLocaleString() : '0'" />
            <StatscardComponent header="Unregistered users"
                :amount="stats.totalUnregisteredUsers ? stats.totalUnregisteredUsers.toLocaleString() : '0'" />
            <StatscardComponent header="Registered users"
                :amount="stats.totalRegisteredUsers ? stats.totalRegisteredUsers.toLocaleString() : '0'" />
        </div>

        <div class="Section__content--graphs1">
            <div class="Section__content--graph1">
                <div v-if="charts.length > 0" class="graph-large">
                    <GraphTemplate :chartHeader="charts[0].header" :chartType="charts[0].type"
                        :chartData="charts[0].data" :chartOptions="charts[0].options"
                        :chartSubtitle="charts[0].subtitle" :customStyles="{width: '100%', height: '100%' }" />
                </div>
            </div>

            <div class="Section__content--graph2">
                <div v-for="(chart) in charts.slice(1,3)" :key="chart.id" class="graphs-small">
                    <GraphTemplate :chartHeader="chart.header" :chartType="chart.type" :chartData="chart.data"
                        :chartOptions="chart.options" :chartSubtitle="chart.subtitle" />
                </div>
            </div>
        </div>

        <div class="Section__content--graph3">
                <div v-for="(chart) in charts.slice(3)" :key="chart.id" class="graph-long">
                    <GraphTemplate :chartHeader="chart.header" :chartType="chart.type" :chartData="chart.data"
                        :chartOptions="chart.options" :chartSubtitle="chart.subtitle" />
                </div>
            </div>
        
    </div>
</template>

<style scoped>
@import "@/assets/styles/Dashboard/Sections/UseranalyticsSection.css";
</style>