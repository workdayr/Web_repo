<script setup>
import { ref, onMounted, nextTick, watch, defineProps } from 'vue';
import { useFavoritesStore } from '@/store/useFavoritesStore';
import { productDetailsService } from '@/api/productDetailsService'
import AddFavoriteButton from '@/components/Common/AddFavoriteButton.vue';
const props = defineProps({
    product_id: String,
    screenWidth: Number
})

const isDescriptionExpanded = ref(false);
const productData = ref(null);
const loading = ref(true);
const selectedImage = ref(null);
const favoritesStore = useFavoritesStore();
const descriptionMaxHeight = ref(6.2);
const isCollapsible = ref(false);
const descriptionContainer = ref(null);

function checkCollapsibility() {
    nextTick(() => {
        if (!descriptionContainer.value) return;

        const container = descriptionContainer.value;
        const maxHeightPx = descriptionMaxHeight.value * parseFloat(getComputedStyle(document.documentElement).fontSize);

        const scrollHeight = container.scrollHeight;
        isCollapsible.value = scrollHeight > maxHeightPx;
    });
}

watch(() => productData.value?.description, () => {
    checkCollapsibility();
});


const toggleDescription = () => {
    isDescriptionExpanded.value = !isDescriptionExpanded.value;
};

const changeImage = (newImage) => {
    selectedImage.value = newImage;
};

const fetchProductData = async () => {
    try {
        const response = await productDetailsService.getProduct(props.product_id);
        productData.value = response.data;
    } catch (err) {
        console.error(err);
    } finally {
        loading.value = false;
    }
};

onMounted(() => {
    fetchProductData();
    checkCollapsibility();
});



const handleFollowChange = (isFavorited) => {
    if (loading.value) return;
    if (isFavorited) {
        favoritesStore.addFavorite(productData.value.product_id);
    } else {
        favoritesStore.removeFavoriteByProductId(productData.value.product_id);
    }
};
</script>

<template>
    <div class="first-half">
        <div v-if="screenWidth >= 766" class="product-section">
            <template v-if="productData && productData.images_URL && productData.images_URL.length > 0">
                <img :src="selectedImage || productData.images_URL[0]" alt="Product Image" class="product-image">

                <div class="thumbnail-container">
                    <img v-for="(thumb, index) in productData.images_URL" :key="index" :src="thumb" alt="Thumbnail"
                        class="thumbnail-image" @click="changeImage(thumb)">
                </div>
            </template>
        </div>
        <div class="product-details">
            <h2 class="product-title">{{ productData?.name || 'Loading name...' }}</h2>
            <div v-if="screenWidth < 766" class="product-section">

                <template v-if="productData && productData.images_URL && productData.images_URL.length > 0">
                    <img :src="selectedImage || productData.images_URL[0]" alt="Product Image" class="product-image">

                    <div class="thumbnail-container">
                        <img v-for="(thumb, index) in productData.images_URL" :key="index" :src="thumb" alt="Thumbnail"
                            class="thumbnail-image" @click="changeImage(thumb)">
                    </div>
                </template>
            </div>
            <p class="price-label">Lowest price:</p>
            <p class="product-price">
                {{ productData?.current_lowest_price?.price
                    ? (productData.current_lowest_price.symbol || '$') + ' ' +
                    parseFloat(productData.current_lowest_price.price).toLocaleString('en-US', {
                        minimumFractionDigits:
                            2, maximumFractionDigits: 2
                })
                : 'Loading price...' }}
            </p>
            <p class="store-product">on {{ productData?.store_name || 'Loading store...' }}</p>

            <div class="description-container" @click="toggleDescription">
                <div class="description-text-container" ref="descriptionContainer"
                    :style="{ '--description-max-height': descriptionMaxHeight + 'rem' }"
                    :class="{ 'collapsed': isCollapsible && !isDescriptionExpanded }">
                    <p class="description-text">
                        {{ productData?.description || 'Loading description...' }}
                    </p>
                    <p class="description-text-highlighted">
                        <span> Brand: </span> {{ productData?.brand_name || 'Loading brand...' }}
                    </p>
                </div>
                <span class="see-button" v-if="isCollapsible && !isDescriptionExpanded">
                    ↓ See more
                </span>
                <span class="see-button" v-if="isCollapsible && isDescriptionExpanded">
                    ↑ See less
                </span>
            </div>
            <div class="favorite-button-container">
                <AddFavoriteButton :isFollowed="favoritesStore.isProductFollowed(productData?.product_id)"
                    @update:isFollowed="handleFollowChange" aria-label="Add to favorites" />
                <p v-if="!favoritesStore.isProductFollowed(productData?.product_id)" class="follow-text">Follow
                    product</p>
                <p v-else class="follow-text">Followed</p>
            </div>
        </div>
    </div>


</template>