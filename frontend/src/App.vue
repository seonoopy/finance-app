<template>
  <div>
    <img alt="Vue logo" src="./assets/logo.png">
    <div>
      <Transactions msg="Welcome to Your Vue.js App"/>
    </div>
  </div>
</template>

<script>
import Transactions from './components/Transactions.vue'

export default {
  name: 'App',
  components: {
    Transactions
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
