<template>
  <div id="app">
    <Alfred/>
  </div>
</template>

<script>
import Alfred from './components/Alfred.vue'

export default {
  name: 'app',
  components: {
    Alfred
  }
}
</script>

<style>
#app {
  /* font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50; */
  /* margin-top: 60px; */
  margin: 20px;
}
</style>
