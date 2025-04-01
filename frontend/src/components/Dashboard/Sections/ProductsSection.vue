<script setup>
import HeaderComponent from '../HeaderComponent.vue';
import GraphTemplate from '@/components/UI/GraphTemplate.vue';
import { fetchProductsChartData } from '@/api/productsChartService';
import { ref, onMounted, defineProps, onUnmounted } from 'vue';


const charts = ref([]);
const screenWidth = ref(window.innerWidth);
const loadData = async () => {
    const { charts: chartData } = await fetchProductsChartData();
    charts.value = chartData;
};
onMounted(loadData);

defineProps({
    src: String,
})

const updateScreenWidth = () => {
  screenWidth.value = window.innerWidth;
};

onMounted(() => {
  window.addEventListener('resize', updateScreenWidth);
});

onUnmounted(() => {
  window.removeEventListener('resize', updateScreenWidth);
});
</script>

<template>
    <div class="content__container">
        <div class="header__container">
            <HeaderComponent text="Products" />
        </div>

        <section class="products__section1">
            <div class="products__products-being-tracked">

                <h2 class="products-being-tracked__header">23,648<br><span>Total products being tracked</span></h2>
                <GraphTemplate v-if="charts.length > 0" :chartType="charts[0].type" :chartData="charts[0].data"
                    :chartOptions="charts[0].options" :customStyles="{
                            width: '100%',
                            height: '150px',
                            maxHeight: '200px'
                        }" />

            </div>
            <div class="products__most-followed-products">
                <h2 class="most-followed-products__header">Most followed products</h2>
                <div class="most-followed-products__list">
                    <div class="list__products">
                        <h3 class="list-header">Products</h3>
                        <div class="list-product">
                            <img src="@/assets/generalIcons/iPhone15Icon.svg" alt="iPhone" />
                            <p>iPhone 14 Pro Max <br>
                                <span>Amazon</span>
                            </p>
                        </div>
                        <div class="list-product">
                            <img src="@/assets/generalIcons/iPhone15Icon.svg" alt="iPhone" />
                            <p>Apple Watch S8 <br>
                                <span>Amazon</span>
                            </p>
                        </div>
                        <div class="list-product">
                            <img src="@/assets/generalIcons/iPhone15Icon.svg" alt="iPhone" />
                            <p>iPhone 15 Pro Max <br>
                                <span>Amazon</span>
                            </p>
                        </div>
                    </div>
                    <div class="list__prices">
                        <h3 class="list__header-prices">Price</h3>
                        <div class="list-price">
                            <p>$1,099.00</p>
                        </div>
                        <div class="list-price">
                            <p>$799.00</p>
                        </div>
                        <div class="list-price">
                            <p>$1,799.00</p>
                        </div>
                    </div>


                </div>
            </div>
        </section>

        <section class="products__section2">
            <div class="products__top-stores-discounts">
                <div v-if="screenWidth >=766" class="graphs-small">
                    <GraphTemplate v-if="charts.length > 0" :chartType="charts[1].type" :chartData="charts[1].data"
                    :chartOptions="charts[1].options" :chartHeader="charts[1].header" :customStyles="{
                            width: '100%',
                            height: '350px',
                            maxHeight: '400px'
                        }" />
                </div>
                <div v-if="screenWidth < 766" class="graphs-small">
                    <GraphTemplate v-if="charts.length > 0" :chartType="charts[1].type" :chartData="charts[1].data"
                    :chartOptions="charts[1].options" :chartHeader="charts[1].header" :chartSubtitle="charts[1].subtitle" :customStyles="{
                            width: '100%',
                            height: '350px',
                            maxHeight: '500px'
                        }" />
                </div>

            </div>
            <div class="products__section2--subsection">
                <div class="products__sale-products">
                    <div class="subsection-header">
                        <img src="@/assets/generalIcons/bagIcon.svg" alt="bag" />
                        <p class="subsection__sale-products--header">Sale products</p>
                    </div>
                    <p class="sale-products__number">756</p>
                </div>
                <div class="products__favorite-products">
                    <div class="subsection-header">
                        <img src="@/assets/generalIcons/Star.svg" alt="bag" />
                        <p class="subsection__favorite-products--header">Sale products</p>
                    </div>
                    <p class="sale-products__number">50.8K</p>
                </div>
                <div class="products__reviews">
                    <div class="subsection__header-reviews">
                        <p class="subsection__reviews--header">Reviews</p>
                        <img src="@/assets/generalIcons/reviewIcons.svg" alt="bag" />
                    </div>
                    <div class="reviews__content">
                        <img src="@/assets/generalIcons/userIcon.svg" alt="user" />
                        <h6 class="reviews__content--username">Sophie Moore</h6>
                        <p class="reviews__content--description">Lorem ipsum dolor sit amet consectetur sed id massa
                            morbi porta malesuada dictumst.</p>
                        <div class="description__edit-button">
                            <img src="@/assets/generalIcons/PencilIcon.svg" alt="user" />
                            <p>Edit</p>
                        </div>
                        
                    </div>
                </div>
            </div>

        </section>

    </div>
</template>

<style scoped>
@import "@/assets/styles/Dashboard/Sections/ProductsSection.css";
</style>