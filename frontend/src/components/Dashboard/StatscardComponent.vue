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
    width: 100%;
    max-height: 100px;
    background: #fff;
    padding: 12px;
    height: 100%;
    border-radius: 5px;
    color: #321647;
    @media(max-width:768px){
        max-height: 60px;
    }
    
}

.statsCard__header {
    font-size: small;
    @media(max-width:768px){
        font-size: x-small;
    }
}

.statsCard__amount {
    font-size: x-large;
    font-weight: 500;
    @media(max-width:768px){
        font-size: small;
    }
}
</style>