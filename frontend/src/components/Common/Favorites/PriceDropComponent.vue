<template>
    <div ref="parent" class="pricedrop__container" @mouseover="togglePopup(true)" @mouseleave="togglePopup(false)">
        <div class="pricedrop__container-icon">
            <svg v-if="priceDrop && !isNaN(priceDrop)" class="pricedrop__icon" :class="{ drop: priceDrop < 0 }" width="15" height="8"
                viewBox="0 0 15 8" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path
                    d="M6.25488 1C6.25488 1.51777 6.67462 1.9375 7.19238 1.9375C7.71015 1.9375 8.12988 1.51777 8.12988 1L6.25488 1ZM7.8553 0.336987C7.48918 -0.0291291 6.89559 -0.0291291 6.52947 0.336987L0.563257 6.3032C0.19714 6.66932 0.19714 7.26291 0.563257 7.62903C0.929373 7.99514 1.52297 7.99514 1.88908 7.62903L7.19238 2.32573L12.4957 7.62903C12.8618 7.99514 13.4554 7.99514 13.8215 7.62903C14.1876 7.26291 14.1876 6.66932 13.8215 6.3032L7.8553 0.336987ZM8.12988 1V0.9999L6.25488 0.9999V1L8.12988 1Z"
                    fill="#D22B2B" />
            </svg>
            <svg v-else width="15" class="pricedrop__icon" height="3" viewBox="0 0 15 3" fill="none"
                xmlns="http://www.w3.org/2000/svg">
                <path d="M1.19238 1.5L13.1924 1.5" stroke="white" stroke-width="1.875" stroke-linecap="round" />
            </svg>
        </div>
        <Teleport to="body">
            <div ref="popup" class="pricedrop__container__text" v-if="displayText">
                <span>Now </span>
                <span class="pricedrop__highlight-text">{{"$"+ Number(currentPrice).toLocaleString() }}</span>
                <span> at </span>
                <span class="pricedrop__highlight-text">{{ store }}</span>
                <template v-if="priceDrop && !isNaN(priceDrop)">
                    <span>{{" "+ priceDrop.toFixed(2) }}</span>%
                    <br>
                    <span v-if="priceDrop > 0">
                        <span class="pricedrop__highlight-text"> Higher </span>
                    </span>
                    <span v-else>
                        <span class="pricedrop__highlight-text"> Lower </span>
                    </span>
                    <span>than price on </span>
                    <span class="pricedrop__highlight-text">{{formatDateToDDMMYY(date)}}</span>
                </template>

            </div>
        </Teleport>
    </div>

</template>

<script setup>
import { defineProps, ref, nextTick } from 'vue'
defineProps({
    currentPrice: Number,
    priceDrop: Number,
    date: String,
    store: String,

});

const displayText = ref(false);

const parent = ref(null);
const popup = ref(null);

const togglePopup = async (display) => {
    displayText.value = display;
    // Wait for Vue to update the DOM
    await nextTick();

    if (displayText.value && parent.value && popup.value) {
        const rect = parent.value.getBoundingClientRect();
        popup.value.style.top = `${rect.top + window.scrollY}px`;
        popup.value.style.left = `${rect.left + window.scrollX}px`;
    }
};
function formatDateToDDMMYY(isoString) {
  const date = new Date(isoString);
  const day = String(date.getDate()).padStart(2, '0');
  const month = String(date.getMonth() + 1).padStart(2, '0'); // months are 0-based
  const year = String(date.getFullYear()).slice(-2); // get last 2 digits

  return `${day}-${month}-${year}`;
}
</script>
<style scoped>
@import "@/assets/styles/Common/Favorites/PriceDropComponent.css";
</style>