import App from './App.vue'
import './bootstrap'
import router from './routes'

window.Vue = Vue

window.axios = axios

window.axios.defaults.headers.common = {
  'X-Requested-With': 'XMLHttpRequest'
};

new Vue({
    el: '#App',
    router,
    render: h => h(App)
})
