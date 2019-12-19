import Vue from 'vue'
import App from './App.vue'
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import VCalendar from 'v-calendar'
import fullCalendar from 'vue-fullcalendar'

Vue.component('full-calendar', fullCalendar)
Vue.config.productionTip = false
Vue.use(BootstrapVue)
// Use v-calendar & v-date-picker components
Vue.use(VCalendar, {
  componentPrefix: 'vc',  // Use <vc-calendar /> instead of <v-calendar />
});

new Vue({
  render: h => h(App),
}).$mount('#app')
