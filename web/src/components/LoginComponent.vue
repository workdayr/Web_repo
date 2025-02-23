<template>
    <div id="login__background">
        <img class="background__shape1" src="@/assets/svg/Vector.svg" alt="Vector">
        <img class="background__shape2" src="@/assets/svg/backgroundShape.svg" alt="backgroundSape">
    </div>
    <div class="login__container">
        <h1 class="login__container--header"> Log In</h1>
        <input class="login__input--username" type="text" placeholder="Username" aria-label="Username">
        <input class="login__input--password" type="text" placeholder="Password" aria-label="Password">
        <div id="login__inputs">
            <label>
                <input id="login__input--rememberMe" type="checkbox" name="Remember me">
                <span class="input__rememberMe--label">Remember me</span>
            </label>
            <a class="login__link--forgotPw" @click="$router.push('/')">Forgot password?</a>
        </div>
        <button class="login__button">NEXT</button>
        <div id="login__other-login-options">
            <p>Other <span class="login__other-login-options--highlited-word">Login </span>options</p>
            <div class="other-login-opitons__icons">
                <img class="GoogleIcon" src="@/assets/svg/Googlelogo.svg" alt="Google">
                <img class="FacebookIcon" src="@/assets/svg/Facebooklogo.svg" alt="Facebook">
                <img class="AppleIcon" src="@/assets/svg/Applelogo.svg" alt="Apple">
            </div>
            <div id="create-account-container">
                <img class="userIcon" src="@/assets/svg/UserIcon.svg" alt="UserIcon"><a class="create-account-container__header">Create account</a>

            </div>


        </div>
    </div>
</template>
<script>
export default {
    name: 'LoginComponent',

}
</script>
<style scoped>
@import "@/assets/styles/LoginComponent.css"
</style>