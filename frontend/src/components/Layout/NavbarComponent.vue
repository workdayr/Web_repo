<template>
	<nav class="navBar__container" :style="{ '--nav-height': navbarHeight + 'px' }" :class="{ 'navBar__search-active': isCompactSearchActive , 'navBar__solid-background':  solidBackground}">
		<LogoComponent :render-title="!isMobile" class="navBar__logo"/>
		<SearchbarComponent v-if="!isMobile" class="navBar__searchBar" text="Search"/>
		<SearchbarCompactComponent v-else class="navBar__searchBar" @toggle-search="openSearchbar($event)"/>
		
		<span v-if="!isMobile" class="navBar__--FQA">FQA</span>
		<span v-if="!isMobile" class="navBar__--Explore">Explore</span>
		<div v-if="!isCompactSearchActive" class="navBar__buttons--container">
			<div v-if="!authStore.isAuthenticated" class="navBar__buttons">
				<button @click="$router.push('/Register')" class="navBar__buttons--SignUp">Sign Up</button>
				<button @click="$router.push('/login')" class="navBar__buttons--Login">Log In</button>
			</div>
			<div v-else class="navBar__buttons logged">
				<FavoritesComponent/>
				<UserAccount/>
			</div>
		</div>
	</nav>
</template>

<script setup>
import LogoComponent from '@/components/UI/LogoComponent.vue';
import SearchbarComponent from '@/components/UI/SearchbarComponent.vue';
import SearchbarCompactComponent from '@/components/UI/SearchbarCompactComponent.vue';
import FavoritesComponent from '@/components/Common/Favorites/FavoritesComponent.vue';
import UserAccount from '@/components/Common/UserAccount.vue';
import { useAuthStore } from '@/store/useAuthStore';
import { ref, onMounted, onUnmounted } from 'vue';

const isCompact = ref(false);

const maxHeight = 80;
const minHeight = 40;
const scrollThreshold = 200;
const navbarHeight = ref(maxHeight);

//mobile navbar
const breakpoint = 992;
const isMobile = ref(window.innerWidth<breakpoint);

const solidBackground = ref(false);

const isCompactSearchActive = ref(false);

const authStore = useAuthStore();

const updateWidth = () => {	
	isMobile.value = window.innerWidth<breakpoint;
	
};

const openSearchbar=(isOpen)=>{
	isCompactSearchActive.value = window.innerWidth< 500 && isOpen;
}

const handleScroll = () => {
	const scrollY = document.documentElement.scrollTop;
	solidBackground.value = scrollY>scrollThreshold;
	navbarHeight.value = Math.max(
		minHeight,
		maxHeight - (scrollY / scrollThreshold) * (maxHeight - minHeight)
	);
};

onMounted(() => {
	if(!isCompact.value) document.addEventListener('scroll', handleScroll);
	window.addEventListener("resize", updateWidth);
});

onUnmounted(() => {
	if(!isCompact.value)document.removeEventListener('scroll', handleScroll);
	window.removeEventListener("resize", updateWidth);
});

</script>

<style scoped>
@import "@/assets/styles/Layout/NavbarComponent.css";
</style>
