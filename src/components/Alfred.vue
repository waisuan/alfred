<template>
  <div>
    <b-alert variant="success" dismissible :show="showAlert" @dismissed="showAlert=false">
      {{ whoIsOnCall }}
    </b-alert>

    <full-calendar :events="fcEvents" locale="en" @eventClick="eventClick"></full-calendar>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Alfred',
  data() {
    return {
      fcEvents: [],
      showAlert: false,
      whoIsOnCall: '',
    }
  },
  methods: {
    'eventClick' (event, jsEvent, pos) {
      console.log('eventClick', event, jsEvent, pos)
      this.showAlert = true
      this.whoIsOnCall = 'BATMAN'
    }
  },
  mounted () {
    this.$nextTick(function () {
      axios.get('http://localhost:8080/alfred-api/event/')
           .then(result => {
            //  console.log(result)
            //  console.log(result['data'])
            //  console.log(result['data']['data'])
            this.fcEvents = result['data']['data']
            //  console.log(this.fcEvents)
            })
    })
  },
  components : {
    'full-calendar': require('vue-fullcalendar')	
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
