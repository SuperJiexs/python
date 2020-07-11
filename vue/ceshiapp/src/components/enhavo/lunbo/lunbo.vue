<template>
  <div class="container">
      <el-carousel :interval="3000"  type="card" height="370px" >
        <el-carousel-item v-for="data in datalist" :key="data.dy_id" style="border-radius: 5px;">
          <div class="dv_img">
            <router-link :to="{path:'/detail/',query:{id:data.dy_id}}">
              <img :src="data.dy_img"  width="230px" height="300px">
            </router-link>
            <div class="dv_xqym">
              <router-link :to="{path:'/detail/',query:{id:data.dy_id}}">
                <h4 style="font-weight: 700;color: hotpink">{{data.dy_name}}</h4>
              </router-link>
              <router-link :to="{path:'/detail/',query:{id:data.dy_id}}">
                <h5 style="margin-top: 10px;color: firebrick">{{ data.dy_zhuyan.slice(0,20)+"..."}}</h5>
              </router-link>
            </div>
          </div>
        </el-carousel-item>
      </el-carousel>
  </div>
</template>

<script>
  import {dys, mvrm} from "../../../apis/apis";

export default {

    name: "lunbo",
    data() {
      return {
        datalist: [],
      }
    },
  methods: {
    getdata() {
      mvrm({}).then(res => {
        this.datalist = res.data.data
      }).catch(err => {
        console.log(err)
      })
    },
  },
  created() {
      this.getdata()
  }

}
</script>

<style scoped lang="css">
  .dv_xqym{
    margin-top: 10px;
  }
  .dv_img{
    height: 400px;
    text-align: center;
    border-radius: 5px;
  }
  .container{
    margin-top: 20px;
    margin-bottom: 20px;
  }
  .el-carousel__item h3 {
    font-size: 14px;
    opacity: 0.75;
    line-height: 370px;
    margin: 0;
  }

</style>
