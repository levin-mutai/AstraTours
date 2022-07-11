import { createApp } from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import axios from 'axios'
import store from './store'
import vmodal from 'vue-js-modal'
// import { BootstrapVue, IconsPlugin,ModalPlugin } from 'bootstrap-vue'
// import 'bootstrap/dist/css/bootstrap.css'
// import 'bootstrap-vue/dist/bootstrap-vue.css'


// axios.defaults.baseURL = "http://167.71.73.235:8001/"  //production
axios.defaults.baseURL = "http://localhost:8000/"  //Development

// BootstrapVue,IconsPlugin,ModalPlugin
createApp(App).use(store).use(router,axios,vmodal).mount('#app')
