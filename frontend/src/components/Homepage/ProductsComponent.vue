<script setup>
import ProductPreview from '@/components/Common/ProductPreview.vue';
</script>

<template>
    <section id="section1--bestSales">
        <h1 class="cardHolder__title--BestSales">Best Sales</h1>
        <div id="cardHolder" class="BestSales">
            <ProductPreview symbol="$" price-whole="9999999" price-fraction="99" title="Monitor LG 24"/>
            <ProductPreview symbol="$" price-whole="9999999" price-fraction="99" title="Monitor LG 24"/>
            <ProductPreview symbol="$" price-whole="9999999" price-fraction="99" title="Monitor LG 24"/>
        </div>
    </section>
    <section id="section2--YouMayAlsoLike">
        <h1 class="cardHolder2__title--YouMayAlsoLike">You may also like</h1>
        <div id="cardHolder2" class="YouMayAlsoLike">
            <div class="cardHolder2__card">
                <div class="cardHolder2__card--description">
                    <h5 class="card2__description--price">$9,999.99</h5>
                    <h5 class="card2__description--product">Monitor LG 24"</h5>
                </div>
            </div>
            <div class="cardHolder2__card">
                <div class="cardHolder2__card--description">
                    <h5 class="card2__description--price">$9,999.99</h5>
                    <h5 class="card2__description--product">Monitor LG 24"</h5>
                </div>
            </div>
            <div class="cardHolder2__card">
                <div class="cardHolder2__card--description">
                    <h5 class="card2__description--price">$9,999.99</h5>
                    <h5 class="card2__description--product">Monitor LG 24"</h5>
                </div>
            </div>
            <div class="cardHolder2__card">
                <div class="cardHolder2__card--description">
                    <h5 class="card2__description--price">$9,999.99</h5>
                    <h5 class="card2__description--product">Monitor LG 24"</h5>
                </div>
            </div>
            <div class="cardHolder2__card">
                <div class="cardHolder2__card--description">
                    <h5 class="card2__description--price">$9,999.99</h5>
                    <h5 class="card2__description--product">Monitor LG 24"</h5>
                </div>
            </div>
            <div class="cardHolder2__card">
                <div class="cardHolder2__card--description">
                    <h5 class="card2__description--price">$9,999.99</h5>
                    <h5 class="card2__description--product">Monitor LG 24"</h5>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
export default {
    name: 'ProductsComponent',
}
</script>

<style scoped>
@import "@/assets/styles/ProductsComponent.css";
</style>