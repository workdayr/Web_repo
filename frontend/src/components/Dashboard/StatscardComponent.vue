<script setup>
import { defineProps } from 'vue';
defineProps({
    header: String,
    amount: String
});
</script>

<template>
    <div class="statsCard">
        <h6 class="statsCard__header">{{ header }}</h6>
        <p class="statsCard__amount">{{ amount }}</p>
    </div>
</template>
<style scoped>
.statsCard {
    width: 30%;
    background: #fff;
    padding: 12px;
    height: 100%;
    border-radius: 5px;
    color: #321647;
}

.statsCard__header {
    font-size: small;
}

.statsCard__amount {
    font-size: x-large;
    font-weight: 500;
}
</style>