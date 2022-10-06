import { createApp } from 'vue'
import App from './App.vue'
import router from "@/router";
import Toast from "vue-toastification";

// Optional, since every component import their Bootstrap functionality
// the following line is not necessary
// import 'bootstrap'

// Import the CSS or use your own!
import "vue-toastification/dist/index.css";

createApp(App)
  .use(router)
  .use(Toast, {})
  .mount('#app')
