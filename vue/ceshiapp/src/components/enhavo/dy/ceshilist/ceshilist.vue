<template>
  <div class="myui-panel_bd clearfix" >
    <sousuo></sousuo>
    <ul class="myui-vodlist clearfix">
      <li v-for=" data in datalist.slice((currentPage-1)*PageSize,currentPage*PageSize)" :key="data.dy_id"
          class="col-lg-6 col-md-6 col-sm-4 col-xs-3 data_li">
        <div class="myui-vodlist__box">
          <router-link :to="{path:'/detail/',query:{id:data.dy_id}}" class="myui-vodlist__thumb lazyload one-pan-link-mark"  :title="data.dy_name">
            <img :src="data.dy_img" class="img_bbx">
          </router-link>
          <div class="myui-vodlist__detail">
            <h4 class="title text-overflow">
              <a href="#">{{data.dy_name}}</a>
            </h4>
            <p class="text text-overflow text-muted hidden-xs">
              {{data.dy_zhuyan}}
            </p>
          </div>
        </div>
      </li>
    </ul>
    <div style="height: 30px"></div>
    <div style="display: flex;justify-content: space-around;">
      <el-pagination @size-change="handleSizeChange"
                     @current-change="handleCurrentChange"
                     background
                     :current-page="currentPage"
                     :page-sizes="pageSizes"
                     :page-size="PageSize" layout="total, sizes, prev, pager, next, jumper"
                     :total="totalCount">
      </el-pagination>
    </div>
  </div>
</template>

<script>
  import sousuo from "./sousuo/sousuo";
  import {dys} from "../../../../apis/apis";

  export default {
    name: "ceshilist",
    data() {
      return {
        datalist: [],
        // 默认显示第几页
        currentPage: 1,
        // 总条数，根据接口获取数据长度(注意：这里不能为空)
        totalCount: 1,
        // 个数选择器（可修改）
        pageSizes: [10, 20],
        // 默认每页显示的条数（可修改）
        PageSize: 20,
      }
    },
    methods: {
      getdata() {
        dys({}).then(res => {
          this.datalist = res.data.data
          this.totalCount = res.data.data.length
        }).catch(err => {
          console.log(err)
        })
      },
      // 每页显示的条数
      handleSizeChange(val) {
        // 改变每页显示的条数
        this.PageSize = val
        // 注意：在改变每页显示的条数时，要将页码显示到第一页
        this.currentPage = 1
      },
      // 显示第几页
      handleCurrentChange(val) {
        // 改变默认的页数
        this.currentPage = val
      },
    },
    components:{
      sousuo
    },
    created() {
      this.getdata()
    }
    // mounted() {
    //     // this.getdata()
    //   fetch('/ct/citys/',{
    //     method:'get',
    //   }).then(res=>{
    //     console.log(res)
    //   }).catch(err=>{
    //     console.log(err)
    //   })
    //
    //
    // }
  }
</script>

<style scoped lang="css">
  .data_li{
    margin-bottom: 10px;
    margin-top: 20px;
  }
  .myui-vodlist{
    background-color: #fff0d6;
    margin-top: 10px;
    margin-bottom: 20px;
  }
  .myui-panel_bd{
    width: 1200px;
    margin-right: auto;
    margin-left: auto;

    border-radius: 5px;
  }
  .img_bbx{
    width: 210px;
    height: 300px;
  }

  .myui-vodlist__thumb {
    display: block;
    position: relative;
    background-position: 50% 50% !important;
    background-size: cover !important;
    overflow: hidden;
    border-radius: 2px;
    box-shadow: 0 1px 2px rgba(0, 0, 0, .1);
  }

  .myui-vodlist__detail .text {
    min-height: 20px;
    font-size: 12px;
    margin-bottom: 0;
    margin-top: 5px;
  }

  .text-muted {
    color: #999395;

  }

  .text-overflow {
    width: 100%;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }

  .myui-vodlist__detail .title {
    margin: 10px 0 0;
    font-size: 15px;
    font-weight: 700;
  }
  .myui-vodlist__box{
    border-radius: 5px;
  }
  .col-lg-6 {
    width: 20%;
    float: left;
    position: relative;
    min-height: 1px;
  }

</style>
