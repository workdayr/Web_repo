<script setup>
import { ref, onMounted, defineProps, watch } from 'vue'; // <-- Import watch
import GraphTemplate from '@/components/UI/GraphTemplate.vue';
import { productDetailsService } from '@/api/productDetailsService';

const props = defineProps({
    product_id: String,
    screenWidth: Number
});

const charts = ref(null);
const loading = ref(true);
const error = ref(null);

const selectedDuration = ref('30'); 

const fetchProductHistoryData = async (productId, duration) => {
    loading.value = true;
    error.value = null;
    try {
        const response = await productDetailsService.fetchProductHistoryChartData(productId, duration);
        if (response && response.chart) {
             charts.value = response.chart;
        } else {
            charts.value = null;
            console.warn("No chart data received or service indicated an error.");
        }
    } catch (err) {
        console.error("Error fetching product history data:", err);
        error.value = "Failed to load chart data.";
        charts.value = null;
    } finally {
        loading.value = false;
    }
};

watch(selectedDuration, (newDuration, oldDuration) => {
    if (newDuration !== oldDuration && !loading.value) { 
         console.log(`Duration changed to: ${newDuration}. Re-fetching...`);
         fetchProductHistoryData(props.product_id, newDuration);
    }
});

onMounted(() => {
    fetchProductHistoryData(props.product_id, selectedDuration.value);
});

</script>

<template>
    <div class="graph__section--graph1">
        <div v-if="loading">Loading Chart...</div>

        <div v-else-if="error">{{ error }}</div>

        <div v-else-if="charts" class="graph-large">
            <div class="product-price-graph_header">
                <h4 class="product-price-graph_title">{{ charts.header }}</h4>

                <select name="duration" id="duration-select" v-model="selectedDuration">
                    <option value="365">1 year</option>
                    <option value="180">6 months</option>
                    <option value="30">1 month</option> 
                    <option value="7">1 week</option>
                </select>
            </div>

            <GraphTemplate
                v-if="screenWidth >= 766"
                :chartType="charts.type"
                :chartData="charts.data"
                :chartOptions="charts.options"
                :customStyles="{
                    width: '100%',
                    height: '400px',
                    maxHeight: '500px'
                }"
            />
            <GraphTemplate
                v-if="screenWidth < 766"
                :chartType="charts.type"
                :chartData="charts.data"
                :chartOptions="charts.options"
                :customStyles="{
                    width: '100%',
                    height: '200px',
                    maxHeight: '500px'
                }"
            />
        </div>

         <div v-else>
             No chart data available.
         </div>
    </div>
</template>

<style scoped>
@import "@/assets/styles/Product/ProductPriceGraph.css";
</style>