<template>
  <HelloWorld msg="Welcome to Your Vue.js App" />
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',
  components: {
    HelloWorld
  }
}
</script>

<style>
body {
  width: 100vw;
  height: 100vh;
  font-family: 'Poppins', sans-serif;
  background: linear-gradient(to right, #121212, #270d27);
}

</style>
