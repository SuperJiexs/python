<template>
  <div id="app">
    <headers></headers>
    <router-view :key="activeDate" />
    <tosto></tosto>
  </div>
</template>


<script>
  import headers from "./components/headers/headers";
  import tosto from "./components/tosto/tosto";

  export default {
    name: 'App',
    components: {
      tosto, headers
    },
    watch:{
      $route:{
        handler(){
          this.activeDate = new Date().getTime()
        },
        immediate:true
      }
    }
  }
</script>

<style scoped>
  html {
    height: 100%;
  }

  * {
    margin: 0;
    padding: 0;
    background-color: #f8f8f8;
    -webkit-box-sizing: border-box;
    -moz-box-sizing: border-box;
    box-sizing: border-box;
    background-position: center;
    background-size: 100%;
  }

</style>
