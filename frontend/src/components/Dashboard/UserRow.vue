<template>
  <template v-for="user in filteredUsers" :key="safeKey(user)">
    <tr v-if="user && isMounted" class="user-row">
      <td>{{ user?.name || '-' }}</td>
      <td>{{ user?.phone || '-' }}</td>
      <td>{{ user?.country || '-' }}</td>
      <td>{{ user?.login_type || '-' }}</td>
      <td>
        <span v-if="user?.status" :class="statusClass(user.status)">
          {{ user.status }}
        </span>
        <span v-else>-</span>
      </td>
      <td v-if="showActions" class="actions">
        <button @click="safeEdit(user)" class="action-btn edit-btn">✏️</button>
        <button @click="safeDelete(user)" class="action-btn delete-btn">
          <img src="@/assets/Common/deleteIcon.svg" alt="Delete Icon">
        </button>
      </td>
    </tr>
  </template>
</template>

<script setup>
import { ref, computed, onMounted, defineProps,defineEmits } from 'vue';

const props = defineProps({
  data: {
    type: Array,
    default: () => []
  },
  showActions: {
    type: Boolean,
    default: true
  }
});

const emit = defineEmits(['delete', 'edit']);
const isMounted = ref(false);

const filteredUsers = computed(() => {
  return props.data?.filter(user => user != null) || [];
});

const safeKey = (user) => {
  return user?.id ?? Math.random().toString(36).substring(2, 9);
};

const safeDelete = (user) => {
  if (user?.id) emit('delete', user.id);
};

const safeEdit = (user) => {
  if (user) emit('edit', user);
};

const statusClass = (status) => {
  if (!status) return '';
  return status === "Online" ? "status online" : "status offline";
};

onMounted(() => {
  isMounted.value = true;
});
</script>

<style scoped>
.user-row {
  background-color: #ffffff;
  color: #321647;
  text-align: left;
  border-bottom: 1px solid #ddd;
}

.user-row td {
  
  font-size: x-small;
  padding: 10px;
}

.status {
  padding: 5px 10px;
  border-radius: 5px;
  font-size: smaller;
}
.online {
  background-color: #26a65b;
  color: #fff;
}
.offline {
  background-color: #f64747;
  color: #fff;
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
}

.edit-btn {
  color: #4caf50;
}

.delete-btn {
  color: #f44336;
}
</style>
