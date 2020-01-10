<template>
  <div id="app">
    <b-navbar type="light" variant="faded">
      <b-navbar-brand>Who is on-call?</b-navbar-brand>
    </b-navbar>
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
@import "https://csshake.surge.sh/csshake.min.css";

#app {
  margin: 5px;
}
</style>
