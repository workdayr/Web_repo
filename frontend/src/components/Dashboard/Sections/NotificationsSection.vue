<script setup>
import HeaderComponent from '../HeaderComponent.vue';
import GraphTemplate from '@/components/UI/GraphTemplate.vue';
import { fetchNotiChartData } from '@/api/notificationsChartService';
import { ref, onMounted } from 'vue';
import TableComponent from '../TableComponent.vue';
import axios from 'axios';
import Swal from 'sweetalert2';
import notificationRow from '../notificationRow.vue';
const charts = ref([]);
const stats = ref({});
const products = ref([]);


const fetchProducts = async () => {
    try {
        const response = await axios.get('http://localhost:8000/api/product/');
        products.value = response.data;
        console.log('Products data:', products.value);
    } catch (error) {
        console.error('Error fetching products:', error);
        // Fallback to sample data if API fails
        products.value = generateSampleData();
    }
};

const confirmDelete = async (productId) => {
    const result = await Swal.fire({
        title: 'Are you sure?',
        text: "You won't be able to revert this!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#d33',
        cancelButtonColor: '#3085d6',
        confirmButtonText: 'Yes, delete it!'
    });

    if (result.isConfirmed) {
        try {
            await axios.delete(`http://localhost:8000/api/product/${productId}/`);
            products.value = products.value.filter(p => p.id !== productId);
            Swal.fire('Deleted!', 'Product has been deleted.', 'success');
        } catch (error) {
            Swal.fire('Error!', 'Failed to delete product.', 'error');
        }
    }
};

const handleEdit = (productId) => {
    console.log('Edit product:', productId);
    // Edit logic here
};

// Sample data generator for development
const generateSampleData = () => {
    const statuses = ['ongoing', 'ends_soon', 'ended'];
    const stores = ['Amazon', 'Mercado Libre', 'AliExpress',  'Walmart'];

    return Array.from({ length: 10 }, (_, i) => ({
        id: i + 1000,
        product_id: `#${i + 1000}`,
        name: `Sample Product ${i + 1}`,
        formatted_date: new Date(Date.now() - Math.random() * 30 * 24 * 60 * 60 * 1000)
            .toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' }),
        status: statuses[i % 3],
        stores: stores.slice(2, Math.floor(Math.random() )),
        formatted_price: new Intl.NumberFormat('en-US', {
            style: 'currency',
            currency: 'USD'
        }).format(Math.random() * 1000 + 10)
    }));
};


const loadNotificationData = async () => {
    const { charts: chartData, stats: statsData } = await fetchNotiChartData();
    charts.value = chartData;
    stats.value = statsData;
};

onMounted(loadNotificationData);
onMounted(fetchProducts);

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
                        :chartOptions="chart.options" :chartSubtitle="chart.subtitle" :customStyles="{
                            width: '100%',
                            height: '300px',
                            maxHeight: '300px'
                        }" />
                </div>
            </div>
        </section>
        <section class="notifications__section2">
            <div class="notifications__best-sales--container">
                <HeaderComponent text="Best sales" color="#321647" fontSize="medium" />
                <TableComponent :headers="['Product ID', 'Product', 'Date', 'Status', 'Stores', 'Price']"
                    :data="products" :show-actions="true">
                    <template #default="{ data }">
                        <notificationRow  :data="data" @delete="confirmDelete" @edit="handleEdit" />
                    </template>
                </TableComponent>



            </div>

        </section>

    </div>



</template>

<style scoped>
@import "@/assets/styles/Dashboard/Sections/NotificationsSection.css";
</style>