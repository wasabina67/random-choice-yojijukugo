<template>
  <div>
    <h1>
      <ruby>
        {{ name }}<rt>{{ name_en }}</rt>
      </ruby>
    </h1>
    <div class="description">
      <p>{{ description }}</p>
      <p>{{ description_en }}</p>
    </div>
  </div>
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
      name: '',
      name_en: '',
      description: '',
      description_en: '',
    }
  },
  mounted() {
    this.nodeEnv = process.env.NODE_ENV
    this.baseUrl = this.nodeEnv === 'production' ? '' : 'http://127.0.0.1:5000'
    this.init()
  },
  methods: {
    async init() {
      try {
        const resp = await axios.get(this.baseUrl + '/api/yojijukugo')
        this.name = resp.data.name
        this.name_en = resp.data.name_en
        this.description = resp.data.description
        this.description_en = resp.data.description_en
      } catch (e) {
        alert(e)
      }
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: left;
  color: #2c3e50;
  margin-top: 30px;
  margin-left: 30px;
}

.description {
  margin-left: 15px;
}
</style>
