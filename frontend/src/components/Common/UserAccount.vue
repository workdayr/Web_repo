<template>
    <div class="user-account__container" @mouseover="hover = true" @mouseleave="hover = false">
        <button class="user-account__button" @click="addToFavorites">
            <svg class="user-account__icon" width="21" height="21" viewBox="0 0 22 23" fill="none"
                xmlns="http://www.w3.org/2000/svg">
                <path
                    d="M12 22.5798C14.6 22.5798 16.96 21.5898 18.74 19.9598C18.64 19.0198 18.04 18.0998 16.97 17.3798C14.25 15.5598 9.77 15.5598 7.03 17.3798C5.96 18.0998 5.36 19.0198 5.26 19.9598C7.04 21.5898 9.4 22.5798 12 22.5798ZM12 22.5798C17.5228 22.5798 22 18.1027 22 12.5798C22 7.05699 17.5228 2.57983 12 2.57983C6.47715 2.57983 2 7.05699 2 12.5798C2 18.1027 6.47715 22.5798 12 22.5798ZM12.12 13.3598C12.05 13.3498 11.96 13.3498 11.88 13.3598C10.12 13.2998 8.72 11.8598 8.72 10.0898C8.72 8.27983 10.18 6.80983 12 6.80983C13.81 6.80983 15.28 8.27983 15.28 10.0898C15.27 11.8598 13.88 13.2998 12.12 13.3598Z"
                    stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
            </svg>
        </button>
        <div v-if="hover" class="user-account__popup">
            <span class="user-account__text">{{ fullName }}</span>
            <span class="user-account__text">{{ authStore.user.email }}</span>
            <button class="user-account__button logout" @click="logout">
                <span class="user-account__text logout">Log out</span>
                <svg width="21" height="21" viewBox="0 0 21 21" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path
                        d="M7.04616 5.98494C7.29158 3.13494 8.75616 1.97119 11.9624 1.97119H12.0653C15.6041 1.97119 17.0212 3.38828 17.0212 6.92702V12.0887C17.0212 15.6274 15.6041 17.0445 12.0653 17.0445H11.9624C8.77991 17.0445 7.31533 15.8966 7.05408 13.0941M11.8753 9.49994H2.86616M4.63158 6.84786L1.97949 9.49994L4.63158 12.152"
                        stroke="#D22B2B" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                </svg>
            </button>
        </div>
    </div>
</template>
<script setup>
import { useAuthStore } from '@/store/useAuthStore';
import { ref } from 'vue'
import { useAuth } from '@/composables/useAuth';
const hover = ref(false);
const authStore = useAuthStore();
const { logout } = useAuth(); 
const fullName = authStore.user.first_name + " " + authStore.user.last_name;

</script>

<style scoped>
@import "@/assets/styles/Common/UserAccount.css";
</style>
