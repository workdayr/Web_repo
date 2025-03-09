<template>
    <footer>
      <div class="footer-content">
        <div class="footer-logo">
          <img :src="BprcsLogo" alt="Bprcs Logo">
        </div>
        <div class="footer-navigation">
          <ul>
            <li><a href="#">Home</a></li>
            <li><a href="#">Profile</a></li>
            <li><a href="#">Log in</a></li>
          </ul>
        </div>
        <div class="footer-learn-more">
          <ul>
            <li><a href="#">About Bprcs</a></li>
            <li><a href="#">Privacy Policy</a></li>
            <li><a href="#">Contact Us</a></li>
          </ul>
        </div>
        <div class="footer-contact">
          <p>Email: <a href="mailto:example.eg@example.com">example.eg@example.com</a></p>
        </div>
        <div class="footer-social">
    <button class="social-button">
      <img src="@/assets/Layout/Footer/facebook-icon.png" alt="Facebook">
    </button>
    <button class="social-button">
      <img src="@/assets/Layout/Footer/twitter-icon.png" alt="Twitter">
    </button>
    <button class="social-button">
      <img src="@/assets/Layout/Footer/instagram-icon.png" alt="Instagram">
    </button>
    <button class="social-button">
      <img src="@/assets/Layout/Footer/linkedin-icon.png" alt="LinkedIn">
    </button>
    <button class="social-button">
      <img src="@/assets/Layout/Footer/youtube-icon.png" alt="YouTube">
    </button>
  </div>
        <div class="footer-bottom">
          <p>© 2025 Bprcs. All rights reserved</p>
          <ul>
            <li><a href="#">Terms & Conditions</a></li>
            <li><a href="#">Privacy Policy</a></li>
            <li><a href="#">Cookies Policy</a></li>
          </ul>
        </div>
      </div>
    </footer>
  </template>
  
  <script>
  import BprcsLogo from '@/assets/Bprcs_logo.png'; // logo
  
  export default {
    name: 'FooterComponent',
    data() {
      return {
        BprcsLogo
      };
    }
  };
  </script>
  
  <style scoped>
  @import "@/assets/styles/Layout/Footer.css";
  </style>