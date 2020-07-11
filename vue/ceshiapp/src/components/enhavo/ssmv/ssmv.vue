<template>
  <div class="container">
    <div class="row">
      <div class="myui-panel myui-panel-bg clearfix" style="margin-top: 50px">
        <div class="myui-panel-box clearfix">
          <div class="myui-panel_head clearfix">
            <h2 class="title">
              <span>{{form}}</span>
            </h2>
          </div>
        </div>
      </div>
      <div class="myui-panel_bd clearfix"  style="background-color: #fff0d6">
        <ul class=" clearfix " >
          <li v-for="data in datalist.slice((currentPage-1)*PageSize,currentPage*PageSize)" :key="data.dy_id" class="clearfix" >
            <div class="li-div" >
              <router-link to="#" tag="a" class="myui-vodlist__thumb">
                <img :src="data.dy_img" width="220px" height="300px">
              </router-link>
            </div >
            <div class="datali" >
              <h4 class="title">
                <router-link to="#" class="">{{data.dy_name}}</router-link>
              </h4>
              <p>
                <span class="text-muted">导演:</span>
                {{data.dy_daoyan}}
              </p>
              <p>
                <span class="text-muted">主演:</span>
                <router-link to="#" class="">{{data.dy_zhuyan.slice(0,30)+"..."}}</router-link>
              </p>
              <p>
                <span class="text-muted">分类:</span>
                {{data.by_type}}
                <span class="split-line">|</span>
                <span class="text-muted">地区:</span>
                {{data.dy_country}}
                <span class="split-line">|</span>
                <span class="text-muted">年份:</span>
                {{data.dy_riqi}}
              </p>
              <p>
                <span class="text-muted">简介:</span>
                {{data.dy_desc.slice(0,60)+"..."}}
              </p>
              <div style="height: 10px"></div>
              <p>
                <router-link to="#">
                  <el-button><i class="el-icon-download">下载按钮</i></el-button>
                </router-link>
                <router-link  :to="{path:'/detail/',query:{id:data.dy_id}}">
                  <el-button type="info" plain>详情按钮<i class="el-icon-arrow-right"></i></el-button>
                </router-link>
              </p>
            </div>
          </li>
        </ul>
      </div>
    </div>
    <div style="display: flex;justify-content: space-around; margin-top: 50px;margin-bottom: 30px">
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
  import {ss} from "../../../apis/apis";

  export default {
    name: "ssmv",
    data() {
      return {
        form:'',
        datalist: [],
        currentPage: 1,
        // 总条数，根据接口获取数据长度(注意：这里不能为空)
        totalCount: 1,
        // 个数选择器（可修改）
        pageSizes: [5,10,15],
        // 默认每页显示的条数（可修改）
        PageSize: 10,
      }
    },
    methods: {
      getdata() {
        ss(this.$route.query.form).then(res => {
          this.form=this.$route.query.form
          this.datalist = res.data.data
          this.totalCount = res.data.data.length
        }).catch(err => {
          console.log(err)
        })
      },
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
    created() {
      this.getdata()
    }
    ,
  }
</script>

<style scoped lang="css">

  .li-div {
    margin: 10px 10px 0 20px;
    padding: 10px;
    float: left;
    border-radius: 5px;
  }
  .datali{
    margin: 10px 0 0 10px;
    padding: 25px;
    float: left;
  }
  div {
    margin: 0;
    padding: 0;
    font-weight: 400;
    display: block;
  }

  h3 {
    display: block;
    font-size: 1.17em;
    margin-block-start: 1em;
    margin-block-end: 1em;
    margin-inline-start: 0px;
    margin-inline-end: 0px;
    font-weight: bold;
  }

  a {
    text-decoration: none;
    outline: none;
  }

  ul {
    display: block;
    list-style-type: disc;
    padding-inline-start: 40px;
    margin-block-start: 1em;
    margin-block-end: 1em;
    margin-inline-start: 0px;
    margin-inline-end: 0px;

  }

  ul li {
    list-style-type: none;
  }


  .container {
    max-width: 1200px;
    position: relative;
    margin-right: auto;
    padding-left: 0px;
    padding-right: 0px;
    margin-left: auto;
  }

  .container:after {
    display: table;
    content: " ";
    clear: both;
  }

  .container:before {
    display: table;
    content: " ";
    clear: both;
  }

  .row:before {
    display: table;
    content: " ";
    clear: both;
  }

  .row:after {
    display: table;
    content: " ";
    clear: both;
  }

  .clearfix:before {
    display: table;
    content: " ";
    clear: both;
  }

  .clearfix:after {
    display: table;
    content: " ";
    clear: both;
  }

  .myui-panel {
    margin-bottom: 20px;
    border-radius: 5px;
    padding: 10px;
    position: relative;
  }

  .myui-panel-bg {
    background-color: #fff;
    box-shadow: 0 1px 3px rgba(0, 0, 0, .05);
  }

  .myui-panel_hd {
    padding: 10px;
  }

  .myui-panel_head {
    position: relative;
    height: 30px;
    margin-right: auto;
    margin-left: auto;

  }

  .myui-panel_head .title {
    font-size: 20px;
    float: left;
    display: inline-block;
    margin: 0;
    padding-right: 10px;
    line-height: 30px;
  }

  .myui-panel_head .more {
    line-height: 30px;
  }


  .text-muted {
    color: #999395;
  }


  .split-line{
    background-color: #eeeeee;
    display: inline-block;
    margin-left: 8px;
    margin-right: 8px;
    width: 1px;
    height: 14px;
  }
  p{
    margin-bottom: 10px;
  }

  li{
    display: list-item;
    text-align: -webkit-match-parent;
  }

  ul, ol, li, p, h1, h2, h3, h4, h5, h6, form, fieldset, table, td, img, tr{
    margin: 0;
    padding: 0;
    font-weight: 400;
  }
  a, h1, h2, h3, h4, h5, h6, h1 a, h2 a, h3 a, h4 a, h5 a, h6 a{
    color: #333333;
  }
  p{
    display: block;
    margin-block-start: 1em;
    margin-block-end: 1em;
    margin-inline-start: 0px;
    margin-inline-end: 0px;
  }
  h4{
    display: block;
    margin-block-start: 1.33em;
    margin-block-end: 1.33em;
    margin-inline-start: 0px;
    margin-inline-end: 0px;
    font-weight: bold;
  }
  .text-muted{
    color: #999395;
  }
  .myui-panel_bd{
    width: 1200px;
    margin-right: auto;
    margin-left: auto
  }


  .container:before, .container:after, .row:before, .row:after, .clearfix:before, .clearfix:after{
    display: table;
    content: ' ';
    clear: both;
  }

  :after,:before{
    -webkit-box-sizing: border-box;
    -moz-box-sizing: border-box;
    box-sizing: border-box;
  }

</style>

