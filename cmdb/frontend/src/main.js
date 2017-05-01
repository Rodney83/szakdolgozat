import App from './App.vue'
import './bootstrap'
import router from './routes'

new Vue({
    el: '#App',
    router,
    render: h => h(App)
})
