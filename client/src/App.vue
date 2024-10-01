<template>
  <img alt="Vue logo" src="./assets/logo.png">
</template>

<script>
import axios from 'axios'

export default {
  name: 'App',
  components: {
  },
  data() {
    return {
      nodeEnv: '',
      baseUrl: '',
    }
  },
  mounted() {
    this.nodeEnv = process.env.NODE_ENV
    this.baseUrl = this.nodeEnv === 'production' ? '' : 'http://127.0.0.1:5000'
    this.init()
  },
  methods: {
    async init() {
      console.log('helloworld')
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
