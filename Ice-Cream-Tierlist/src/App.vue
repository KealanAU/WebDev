<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <TierList/>
    <ItemsSortComp/>
  </div>
</template>

<script>
import TierList from './components/TierList.vue'
import ItemsSortComp from './components/ItemsSortComp.vue'

export default {
  name: 'app',
  components: {
    TierList,
    ItemsSortComp
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
