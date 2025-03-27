<script setup>
import HeaderComponent from '../HeaderComponent.vue';
import GraphTemplate from '@/components/UI/GraphTemplate.vue';
import { fetchNotiChartData } from '@/api/notificationsChartService';
import ProducttableComponent from '../ProducttableComponent.vue';
import { ref, onMounted } from 'vue';

const charts = ref([]);
const stats = ref({});

const loadNotificationData = async () => {
    const { charts: chartData, stats: statsData } = await fetchNotiChartData();
    charts.value = chartData;
    stats.value = statsData;
};
onMounted(loadNotificationData);

</script>

<template>
    <div class="content__container">
        <div class="header__container">
            <HeaderComponent text="Notifications" />
        </div>
        <section class="notifications__section1">
            <div class="notifications__effective-alert-timing">
                <div v-if="charts.length > 0" class="graph-large">
                    <GraphTemplate v-if="charts[0]" :chartHeader="charts[0].header" :chartType="charts[0].type"
                        :chartData="charts[0].data" :chartOptions="charts[0].options" :customStyles="{
                            width: '100%',
                            height: '350px',
                            maxHeight: '500px'
                        }" />
                </div>
            </div>
            <div class="notifications__redictered-users">
                <div v-for="(chart) in charts.slice(1, 2)" :key="chart.id" class="graph-doughnut">
                    <GraphTemplate :chartHeader="chart.header" :chartType="chart.type" :chartData="chart.data"
                        :chartOptions="chart.options" :chartSubtitle="chart.subtitle"
                        :customStyles="{
                            width: '100%',
                            height: '300px',
                            maxHeight: '300px'
                        }" />
                </div>
            </div>
        </section>
        <section class="notifications__section2">
            <div class="notifications__best-sales--container">
                
                <ProducttableComponent />


            </div>

        </section>

    </div>



</template>

<style scoped>
@import "@/assets/styles/Dashboard/Sections/NotificationsSection.css";
</style>