<template>
    <div class="table-container">
        <table class="data-table">
            <thead>
                <tr>
                    <th v-for="header in headers" :key="header">
                        {{ header }}
                    </th>
                    <th v-if="showActions" class="actions-header"></th>
                </tr>
            </thead>
            <tbody>
                <slot name="default" :data="data"></slot>
            </tbody>
        </table>
    </div>
</template>

<script setup>
import { defineProps } from 'vue';
defineProps({
    headers: Array,
    data: Array,
    showActions: {
        type: Boolean,
        default: true
    }
});
</script>

<style scoped>
.table-container {
    padding: 20px;
    border-radius: 10px;
    color: #321647;
    max-width:100%;
    margin: 0 auto;
    height: 90%;
    overflow-y: auto;
}

.data-table {
    width: 100%;
    border-collapse: collapse;
}

.data-table th,
.data-table td {
    font-size: x-small;
    padding: 12px;
    text-align: left;
    border-bottom: 1px solid #ddd;
}

.data-table th {
    background-color: #ffffff;
    color: #321647;
    border-bottom: 1px solid #321647;
    font-size: x-small;
}

.actions-header {
    width: 80px;
    text-align: center;
}
</style>