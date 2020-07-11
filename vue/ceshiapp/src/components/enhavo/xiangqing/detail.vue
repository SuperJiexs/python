<template>
  <div>
    <p>detail</p>
  </div>
</template>

<script>
  import {xq} from "../../../apis/apis";

  export default {
    name: "detail",
    data(){
      return{
        datalist:[],
      }
    },
    methods:{
      getdata(){
        xq(this.$route.query.id).then(res=>{
          this.datalist=res.data.data
        }).catch(err=>{
          console.log(err)
        })
      }
    },created() {
      this.getdata()
    }
  }
</script>

<style scoped>

</style>
