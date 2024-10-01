<template>
  <div>
    <h1>
      <ruby>
        {{ name }}<rt>{{ nameEn }}</rt>
      </ruby>
    </h1>
    <p>{{ description }}</p>
    <p>{{ descriptionEn }}</p>
    <button @click="init">次へ</button>
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
      nameEn: '',
      description: '',
      descriptionEn: '',
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
        this.nameEn = resp.data.name_en
        this.description = resp.data.description
        this.descriptionEn = resp.data.description_en
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

button {
  margin-top: 15px;
}
</style>
