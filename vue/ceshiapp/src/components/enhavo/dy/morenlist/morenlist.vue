<template>
  <div class="myui-panel_bd clearfix">
    <ul class="myui-vodlist clearfix">
      <li v-for=" data in datalist.slice(0,10)" :key="data.dy_id" class="col-lg-6 col-md-6 col-sm-4 col-xs-3 data_li ">
        <div class="myui-vodlist__box">
          <router-link class="myui-vodlist__thumb lazyload one-pan-link-mark" :to="{path:'/detail/',query:{id:data.dy_id}}" :title="data.dy_name">
            <img :src="data.dy_img" class="img_bbx">
          </router-link>
          <div class="myui-vodlist__detail">
            <h4 class="title text-overflow">
              <router-link  tag="a" :to="{path:'/detail/',query:{id:data.dy_id}}">{{data.dy_name}}</router-link>
            </h4>
            <p class="text text-overflow text-muted hidden-xs">
              {{data.dy_zhuyan}}
            </p>
          </div>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
  import {dys} from "../../../../apis/apis";

  export default {
    name: "morenlist",
    data() {
      return {
        datalist:[],
      }
    },
    methods: {
      getdata() {
        dys({}).then(res => {
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
  .data_li{
    margin-bottom: 10px;
    margin-top: 20px;
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

  .myui-panel_bd{
    width: 1200px;
    margin-right: auto;
    margin-left: auto;
    background-color: #fff0d6;
    border-radius: 5px;
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

  p {
    display: block;
    margin-block-start: 1em;
    margin-block-end: 1em;
    margin-inline-start: 0px;
    margin-inline-end: 0px;
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
  .myui-vodlist{
    margin: 0;
    padding: 0;
  }
</style>
