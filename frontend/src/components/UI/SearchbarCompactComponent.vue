    <script setup>
    import {defineProps, ref, defineEmits} from 'vue';
    import SearchbarComponent from '@/components/UI/SearchbarComponent.vue';
    defineProps({
        text:String
    });
    const emit = defineEmits(['toggle-search']);
    const isSearchbarOpen =  ref(false);

    const searchbarRef = ref(null);

    const toggleSearch = () => {
        isSearchbarOpen.value = !isSearchbarOpen.value;
        emit('toggle-search', isSearchbarOpen.value);
    };
    </script>

    <template>
        <div class="icon-bar-container">
            <svg v-if="!isSearchbarOpen" class="main-search-icon" alt="Search Icon" @click="toggleSearch" width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M7.25894 12.9446C10.5317 12.9446 13.1849 10.2915 13.1849 7.0187C13.1849 3.7459 10.5317 1.09277 7.25894 1.09277C3.98614 1.09277 1.33301 3.7459 1.33301 7.0187C1.33301 10.2915 3.98614 12.9446 7.25894 12.9446Z" stroke="#AEB9E1" stroke-linecap="round" stroke-linejoin="round"/>
                <path d="M14.6666 14.4261L11.4443 11.2039" stroke="#AEB9E1" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
            <Transition name="slide">
                <SearchbarComponent ref="searchbarRef" v-if="isSearchbarOpen" @blur="toggleSearch" text="search" :focus="true"/>
            </Transition>
        </div>
    </template>

    <style scoped>  
    @import "@/assets/styles/UI/SearchbarComponent.css";
    </style>