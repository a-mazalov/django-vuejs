import Vue from 'vue'
import App from '@/App.vue'

import store from '@/store'
import router from '@/router'
import vuetify from './plugins/vuetify';

Vue.config.productionTip = false

// Vue.use(VueRouter)

new Vue({
    router,
    store,
    vuetify,
    render: h => h(App)
}).$mount('#app')