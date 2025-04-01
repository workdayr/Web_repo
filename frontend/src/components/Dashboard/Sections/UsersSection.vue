<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import axios from 'axios';
import SearchbarComponent from '@/components/UI/SearchbarComponent.vue';
import HeaderComponent from '../HeaderComponent.vue';
import StatscardComponent from '../StatscardComponent.vue';
import TableComponent from '../TableComponent.vue';
import UserRow from '../UserRow.vue';
import Swal from 'sweetalert2';
import SearchbarCompactComponent from '@/components/UI/SearchbarCompactComponent.vue';


const statsData = ref([
    { header: "Total users" },
    { header: "New users" },
    { header: "Top users" },
    { header: "Other users" }
]);

const users = ref([]);
const screenWidth = ref(window.innerWidth);
const isCompactSearchActive = ref(false);


const updateScreenWidth = () => {
  screenWidth.value = window.innerWidth;
};

onMounted(() => {
  window.addEventListener('resize', updateScreenWidth);
});

onUnmounted(() => {
  window.removeEventListener('resize', updateScreenWidth);
});

const openSearchbar=(isOpen)=>{
	isCompactSearchActive.value = window.innerWidth< 500 && isOpen;
}

const fetchUsers = async () => {
    try {
        const response = await axios.get("http://localhost:8000/api/user-records/");
        users.value = response.data;
    } catch (error) {
        console.error("Error fetching users:", error);
    }
};


const handleDeleteUser = async (id) => {
    const result = await Swal.fire({
        title: 'Confirm Deletion',
        text: "You won't be able to revert this!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#d33',
        cancelButtonColor: '#3085d6',
        confirmButtonText: 'Yes, proceed!'
    });

    if(result.isConfirmed){
    try {
        await axios.delete(`http://localhost:8000/api/user-records/${id}/`);
        users.value = users.value.filter(user => user.id !== id);
        Swal.fire('Deleted!', 'User has been deleted.', 'success');
    } catch (error) {
        console.error("Error deleting user:", error);
    }
}
};





onMounted(fetchUsers);
</script>

<template>
    <section class="users__header-container">
        <HeaderComponent text="Users" />
        <SearchbarComponent v-if="screenWidth >= 766"  text="Search for..." color="#321647" background="#FFF" width="44%" height="30px"
            marginLeft="5%" />
            <SearchbarCompactComponent v-if="screenWidth < 766" class="navBar__searchBar" @toggle-search="openSearchbar($event)"/>
            <div class="users__header-buttons--container">
            <button class="header__buttons--search-user">Search User</button>
            <button class="header__buttons--add-user">Add User</button>
        </div>
    </section>

    <section class="users__content-container">
        <div class="users__statcards-container">
            <StatscardComponent v-for="(stat, index) in statsData" :key="index" :header="stat.header" />
        </div>
        <div class="users__all-users--container">
            <HeaderComponent v-if="screenWidth >= 766" text="All users" color="#321647" fontSize="medium" />
            <HeaderComponent v-if="screenWidth < 766" text="All users" responsive-color="#321647" responsive-font-size="small" responsive-margin-left="5%" />
            <TableComponent :headers="['Name', 'Phone', 'Country', 'Log In', 'Status']" :data="users">
                <template #default="{ data }">
                    <UserRow :data="data" @delete="handleDeleteUser" />
                </template>
            </TableComponent>
        </div>
    </section>
</template>

<style scoped>
@import "@/assets/styles/Dashboard/Sections/UsersSection.css";
</style>