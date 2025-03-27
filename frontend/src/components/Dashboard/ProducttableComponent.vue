<template>
    <div class="product-section">
      <div class="product-header">
        <HeaderComponent class="best-sales__header" text="Best sales" color='#321647' fontSize="medium" />
        <select v-model="selectedDate" @change="fetchProducts">
          <option v-for="month in months" :key="month.value" :value="month.value">{{ month.label }}</option>
        </select>
      </div>
      <table class="product-table">
        <thead>
          <tr>
            <th>Product ID</th>
            <th>Product</th>
            <th>Date</th>
            <th>Status</th>
            <th>Stores</th>
            <th>Price</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="product in products" :key="product.id">
            <td>{{ product.product_id }}</td>
            <td>{{ product.name }}</td>
            <td>{{ formatDate(product.date) }}</td>
            <td>
              <span :class="statusClass(product.status)">
                {{ formatStatus(product.status) }}
              </span>
            </td>
            <td>{{ product.store }}</td>
            <td>${{ product.price.toLocaleString() }}</td>
            <td class="actions">
              <button class="edit-btn"><i class="fas fa-pencil-alt"></i></button>
              <button class="delete-btn"><i class="fas fa-trash"></i></button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script setup>
  import HeaderComponent from "./HeaderComponent.vue";
  import { ref, onMounted } from "vue";
  
  const products = ref([]);
  const selectedDate = ref("");
  const months = ref([
    { label: "Jan 2024", value: "2024-01" },
    { label: "Feb 2024", value: "2024-02" },
    { label: "Mar 2024", value: "2024-03" },
    { label: "Apr 2024", value: "2024-04" },
  ]);
  
  const fetchProducts = async () => {
    try {
      const url = selectedDate.value
        ? `http://127.0.0.1:8000/api/products/?date=${selectedDate.value}`
        : "http://127.0.0.1:8000/api/products/";
      const response = await fetch(url);
      const data = await response.json();
      products.value = data;
    } catch (error) {
      console.error("Error fetching products:", error);
    }
  };
  
  const formatDate = (dateStr) => {
    const dateObj = new Date(dateStr);
    return dateObj.toLocaleDateString("en-US", { year: "numeric", month: "short", day: "numeric" });
  };
  
  const formatStatus = (status) => {
    const statusMap = {
      ongoing: "✔ On going",
      ended: "✖ Ended",
      ends_soon: "⚠ Ends soon",
    };
    return statusMap[status] || status;
  };
  
  const statusClass = (status) => {
    return {
      ongoing: "status-on",
      ended: "status-ended",
      ends_soon: "status-warning",
    }[status];
  };
  
  onMounted(fetchProducts);
  </script>
  
  <style scoped>
  .product-section {
    background: #ffffff;
    padding: 20px;
    border-radius: 15px;
  }
  .product-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 15px;
  }
  .product-table {
    width: 100%;
    border-collapse: collapse;
  }
  .product-table th, .product-table td {
    padding: 12px;
    text-align: left;
    border-bottom: 1px solid #ffffff;
    color: #321647;
    font-size: x-small;
  }
  .product-table th {
    background-color: #ffffff;
  }
  .status-on {
    color: #28a745;
  }
  .status-ended {
    color: #dc3545;
  }
  .status-warning {
    color: #ffc107;
  }
  .actions button {
    background: none;
    border: none;
    cursor: pointer;
    margin: 0 5px;
  }
  .edit-btn i {
    color: #28a745;
  }
  .delete-btn i {
    color: #dc3545;
  }
  </style>
  