<template>
  <div class="centered">
    <!-- <b-alert variant="success" dismissible :show="showAlert" @dismissed="showAlert=false">
      {{ whoIsOnCall }}
    </b-alert>

    <full-calendar :events="fcEvents" locale="en" @eventClick="eventClick"></full-calendar> -->
    <b-card-group deck>

      <b-card bg-variant="secondary" text-variant="white" header="Previous" class="custom-card">
        <b-card-text v-show="previousOnCall">
          {{ previousOnCall }}
        </b-card-text>
        <b-card-text v-show="!previousOnCall">
          <b-spinner small label="Small Spinner"></b-spinner>
        </b-card-text>
      </b-card>

      <b-card border-variant="primary" header-bg-variant="primary" header-text-variant="white" header="Current" class="text-center" :class="customEffect">
        <b-card-text v-show="currentOnCall">
          {{ currentOnCall }}
        </b-card-text>
        <b-card-text v-show="!currentOnCall">
          <b-spinner small label="Small Spinner"></b-spinner>
        </b-card-text>
      </b-card>

      <b-card bg-variant="success" text-variant="white" header="Next" class="custom-card">
        <b-card-text v-show="nextOnCall">
          {{ nextOnCall }}
        </b-card-text>
        <b-card-text v-show="!nextOnCall">
          <b-spinner small label="Small Spinner"></b-spinner>
        </b-card-text>
      </b-card>
    </b-card-group>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Alfred',
  data() {
    return {
      customEffect: '',
      currentOnCall: '',
      previousOnCall: '',
      nextOnCall: ''
    }
  },
  methods: {
    refresh_data: function(updated_data) {
      if (this.currentOnCall != updated_data['current']['team']) {
        this.customEffect = 'shake-slow shake-constant'
        var self = this
        setTimeout(function(){
          self.customEffect = ''
        }, 2000)
      }
      this.currentOnCall = updated_data['current']['team']
      this.previousOnCall = updated_data['previous']['team']
      this.nextOnCall = updated_data['next']['team']
    }
  },
  mounted () {
    // this.$nextTick(function () {
    //   axios.get('http://localhost:8080/alfred-api/event/')
    //        .then(payload => {
    //           console.log(payload)
    //           this.refresh_data(payload['data'])
    //         })
    // })

    this.$options.sockets.onmessage = function(payload) {
      console.log(payload)
      var data = JSON.parse(payload['data'])
      this.refresh_data(data);
    }
  },
  components : {
    'full-calendar': require('vue-fullcalendar')
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.centered {
  margin-top: 15%;
  margin-left: 65px;
  margin-right: 65px;
}

.custom-card {
  text-align: center;
  opacity: 0.5;
}
</style>
