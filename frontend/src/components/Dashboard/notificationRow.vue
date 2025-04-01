<template>
    <tr v-for="item in data" :key="item.id" class="notification-row">
        <td>{{ item.product_id || 'N/A' }}</td>
        <td>{{ item.name || 'N/A' }}</td>
        <td>{{ item.formatted_date || 'N/A' }}</td>
        <td>
            <span :class="statusClass(item.status)">
                {{ formatStatus(item.status) }}
            </span>
        </td>
        <td>
            <span v-for="store in item.stores" :key="store" class="store-tag">
                {{ store }}
            </span>
            <span v-if="!item.stores || item.stores.length === 0">N/A</span>
        </td>
        <td>{{ item.formatted_price || 'N/A' }}</td>
        <td v-if="showActions" class="actions">
            <button @click="$emit('edit', item.id)" class="action-btn edit-btn">
                ✏️
            </button>
            <button @click="$emit('delete', item.id)" class="action-btn delete-btn">
                <img src="@/assets/Common/deleteIcon.svg" alt="Delete Icon">
            </button>
        </td>
    </tr>
</template>

<script setup>
import { defineProps } from 'vue';

defineProps({
    data: {
        type: Array,
        required: true,
        default: () => []
    },
    showActions: {
        type: Boolean,
        default: true
    }
});

const formatStatus = (status) => {
    const statusMap = {
        'ongoing': 'On going',
        'ends_soon': 'Ends soon',
        'ended': 'Ended'
    };
    return statusMap[status] || status;
};

const statusClass = (status) => {
    const classes = {
        'ongoing': 'status-ongoing',
        'ends_soon': 'status-ends-soon',
        'ended': 'status-ended'
    };
    return classes[status] || '';
};
</script>

<style scoped>
.notification-row{
    font-size: 60%;
    @media(max-width: 768px){
        font-size: 50%;
        text-align: center;
}
}

.store-tag {
    display: inline-block;
    background: #FFF;
    padding: 4px 8px;
    border-radius: 4px;
    margin: 2px;
}

.status-ongoing {
    background-color: #26a65b;
    color: white;
    padding: 4px 8px;
    border-radius: 4px;
    @media(max-width: 768px){
        padding: 3px;
}
}

.status-ends-soon {
    background-color: #f39c12;
    color: white;
    padding: 4px 8px;
    border-radius: 4px;
    @media(max-width: 768px){
        padding: 3px;
}
}

.status-ended {
    background-color: #e74c3c;
    color: white;
    padding: 4px 8px;
    border-radius: 4px;
    @media(max-width: 768px){
        padding: 3px;
}
}

.actions {
  display: flex;
  flex-direction: row;
  text-align: center;
  width: 80px;
  
}

.action-btn {
  background: none;
  border: none;
  cursor: pointer;
  margin: 0 4px;
  font-size: 16px;
  @media(max-width: 768px){
    font-size: 12px;
}
}
</style>