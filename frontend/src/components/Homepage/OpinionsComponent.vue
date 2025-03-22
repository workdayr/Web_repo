<template>
    <h1 class="cardHolder__title--Opinions">What people think about us?</h1>
    <section id="Opinions">
        <div id="cardHolder__Opinions" class="Opinions">
            <div class="cardHolder__card--Opinions">
                <h5 class="card__username">{{ Username1 }}</h5>
                <p class="card__opinion">
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore
                    et
                    dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
                    aliquip
                    ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum
                    dolore
                </p>
                <img class="reviewStars" :src="stars" alt="reviewStars">
                <button class="card__button">Answer</button>
            </div>
            <div class="cardHolder__card--Opinions">
                <h5 class="card__username">{{ Username2 }}</h5>
                <p class="card__opinion">
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore
                    et
                    dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
                    aliquip
                    ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum
                    dolore
                </p>
                <img class="reviewStars" :src="stars" alt="reviewStars">
                <button class="card__button">Answer</button>
            </div>
            <div class="cardHolder__card--Opinions">
                <h5 class="card__username">{{ Username3 }}</h5>
                <p class="card__opinion">
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore
                    et
                    dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
                    aliquip
                    ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum
                    dolore
                </p>
                <img class="reviewStars" :src="stars" alt="reviewStars">
                <button class="card__button">Answer</button>
            </div>
        </div>
        <div class="shareOp__button--container">
            <button class="shareOp__button">Share your opinion</button>
        </div>
    </section>

</template>

<script>
import stars from '@/assets/generalIcons/stars.png';
export default {
    name: 'OpinionsComponent',
    props: ['Username1', 'Username2', 'Username3'],
    data() {
        return {
            stars
        };

    }
};

</script>

<style scoped>
@import "@/assets/styles/Homepage/OpinionsComponent.css";
</style>