<template>

  <head>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link
      href="https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&family=Montserrat:ital,wght@0,100..900;1,100..900&family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap"
      rel="stylesheet">
    <title>Index</title>
  </head>
  <body>
  <section id="Homepage">
    <nav class="Homepage__navBar">
      <a class="navBar__BprcsLogo" href="http://localhost:8080/?#">
        <img :src="BprcsLogo" alt="Bprcs_logo">
      </a>
      <input class="navBar__searchBar" type="search" placeholder="Search" aria-label="Search">
      <li class="navBar__li--FQA">FQA</li>
      <li class="navBar__li--Explore">Explore</li>
      <div class="navBar__buttons">
        <button class="navBar__buttons--SignUp">Sign Up</button>
        <button class="navBar__buttons--Login">Log In</button>
      </div>
    </nav>
  </section>
  </body>
</template>

<script>
import BprcsLogo from '@/assets/Bprcs_logo.png';
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  data() {
    return {
      BprcsLogo
    };
  }
}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .Homepage__navBar{
    height: 60px;
    display: flex;
    position: absolute;
      top: 29.73px;
  }

  li{
    font-size: 13px;
    color: #FFFF;
    display: inline-block;
    margin-left: 50px;
    padding-top:20px;
  }
  .navBar__buttons--SignUp,.navBar__buttons--Login{
    font-size: 11px;
    display:inline-block;
    width:90px;
    margin: 12px;
    padding: 8px;
    border-radius:30px;
  }
  .navBar__buttons--SignUp{
    
    margin-left: 60px;
    background-color: transparent;
    color: #FFFF;
    border: 1px solid #FFFF;
    }

    .navBar__buttons--Login{
    
    margin-left: 20px;
    font-weight:lighter;
    background-color: #FFFF;
    color: #0D0E36;
    border: transparent;
    }

    .navBar__searchBar{
      border-radius: 20px;
      border: 1px solid #FFFF;
      width: 422px;
      height: 30px;
      margin: 12px;
      margin-left:100px;
    }
    .navBar__BprcsLogo img{
      display: inline-block;
      width: 120px;
      height: auto;
      max-width: 100%;
      padding-top: 12px;
      margin-left: 60px;
    }


</style>
