<script setup>
import { ref, onMounted, onUnmounted } from "vue";
import HeaderComponent from "../HeaderComponent.vue";
import StatscardComponent from "../StatscardComponent.vue";
import GraphTemplate from "@/components/UI/GraphTemplate.vue";
import { fetchChartData } from "@/api/userChartService";
import { Chart, registerables } from "chart.js";
Chart.register(...registerables)

const charts = ref([]);
const stats = ref({});
const screenWidth = ref(window.innerWidth);

const loadData = async () => {
    const { charts: chartData, stats: statsData } = await fetchChartData();
    charts.value = chartData;
    stats.value = statsData;
};
const updateScreenWidth = () => {
  screenWidth.value = window.innerWidth;
};

onMounted(() => {
  window.addEventListener('resize', updateScreenWidth);
});

onUnmounted(() => {
  window.removeEventListener('resize', updateScreenWidth);
});

onMounted(loadData);


</script>

<template>
    <div class="Section__content">

        <HeaderComponent  text="User Analytics" />

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
                    <GraphTemplate v-if="screenWidth >= 766" :chartHeader="charts[0].header" :chartType="charts[0].type"
                        :chartData="charts[0].data" :chartOptions="charts[0].options"
                        :chartSubtitle="charts[0].subtitle" :customStyles="{
                            width: '100%',
                            height: '370px',
                            maxHeight: '500px'
                        }" />
                     <GraphTemplate v-if="screenWidth < 766" :chartHeader="charts[0].header" :chartType="charts[0].type"
                        :chartData="charts[0].data" :chartOptions="charts[0].options"
                        :chartSubtitle="charts[0].subtitle" :customStyles="{
                            width: '100%',
                            height: '300px',
                            maxHeight: '300px'
                        }" />    
                </div>
            </div>

            <div class="Section__content--graph2">
                <div v-for="(chart) in charts.slice(1, 3)" :key="chart.id" class="graphs-small">
                    <GraphTemplate v-if="screenWidth >= 766" :chartHeader="chart.header" :chartType="chart.type" :chartData="chart.data"
                        :chartOptions="chart.options" :chartSubtitle="chart.subtitle" :customStyles="{
                            width: '100%',
                            height: '170px',
                            maxHeight: '200px',
                            marginBottom: '20px'
                        }"/>
                </div>
                <div v-if="screenWidth < 766" class="graph2__responsive-container">
                <div v-for="(chart) in charts.slice(1, 3)" :key="chart.id" class="graphs-small">
                    <GraphTemplate  :chartHeader="chart.header" :chartType="chart.type" :chartData="chart.data"
                        :chartOptions="chart.options" :chartSubtitle="chart.subtitle" :customStyles="{
                            width: '100%',
                            height: '200px',    
                            maxHeight: '200px',
                            marginBottom: '40px'
                        }"/>
                </div>
            </div>
            </div>
        </div>

        <div class="Section__content--graph3">
            <div v-if="charts.length > 0" class="graph-large">
                    <GraphTemplate v-if="screenWidth >= 766" :chartHeader="charts[3].header" :chartType="charts[0].type"
                        :chartData="charts[3].data" :chartOptions="charts[3].options"
                        :chartSubtitle="charts[3].subtitle" :customStyles="{
                            width: '100%',
                            height: '200px',
                            maxHeight: '200px'
                        }" />
            </div>
            <div v-if="charts.length > 0 && screenWidth < 766" class="graph-large">
                    <GraphTemplate :chartHeader="charts[3].header" :chartType="charts[0].type"
                        :chartData="charts[3].data" :chartOptions="charts[3].options"
                        :chartSubtitle="charts[3].subtitle" :customStyles="{
                            width: '100%',
                            height: '250px',
                            maxHeight: '500px'
                        }" />
            </div>
        </div>

    </div>
</template>

<style scoped>
@import "@/assets/styles/Dashboard/Sections/UseranalyticsSection.css";
</style>