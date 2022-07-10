import { createApp } from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import axios from 'axios'
import store from './store'

// axios.defaults.baseURL = "http://167.71.73.235:8001/"  //production
axios.defaults.baseURL = "http://localhost:8000/"  //Development


createApp(App).use(store).use(router,axios).mount('#app')
