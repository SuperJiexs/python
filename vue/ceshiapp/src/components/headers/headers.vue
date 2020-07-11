<template>
  <div class="headers" >
    <div></div>
    <div class="headers-top">
      <div class="headers-top-c">
        <div class="headers-l headers-wei">
          <router-link to="/">shouye</router-link>
          <span class="sap">|</span>
          <router-link to="/ceshi">dianying</router-link>
          <span class="sap">|</span>
          <router-link to="#">dianshiju</router-link>
          <span class="sap">|</span>
          <router-link to="#">dongman</router-link>
          <span class="sap">|</span>
          <router-link to="#">zongyi</router-link>
        </div>
        <div class="headers-r">
          <a href="#">
            <Icon type="ios-cart" />
            购物车
            <span>(0)</span>
          </a>

          <!-- 购物车下拉列表<div></div>-->
        </div>
        <div class="headers-c">
          <a href="#" >
            <Icon type="ios-contact" />
            登陆
          </a>
          <span class="sap">|</span>
          <a href="#" >注册</a>
          <span class="sap">|</span>
          <router-link to="#" tag="a">意见反馈</router-link>
          <span class="sap">|</span>
          <span class="sap-mass">
              <a href="#">
                <Icon type="md-text"/>
                消息列表
              </a>
            </span>
        </div>
      </div>
    </div>

    <div class="headers-mal">
      <div class="headers-top-c">
        <div class="headers-mal-l">
          <router-link to="#" class="logo logo1">logo</router-link>
        </div>
        <div class="headers-mal-c">
          <ul class="headers-mal-c-ul ul-before" >
            <li class="list-head">  </li>
            <li class="list-l">
              <router-link to="#" class="link">
                <span>zhanzheng</span>
              </router-link>
            </li>
            <li class="list-l">
              <router-link to="#" class="link">
                <span>aiqing</span>
              </router-link>
            </li>
            <li class="list-l">
              <router-link to="#" class="link">
                <span>juqing</span>
              </router-link>
            </li>
            <li class="list-l">
              <router-link to="#" class="link">
                <span>kehuan</span>
              </router-link>
            </li>
            <li class="list-l">
              <router-link to="#" class="link">
                <span>xiju</span>
              </router-link>
            </li>

          </ul>
        </div>
        <div class="headers-mal-r">
          <div style="height: 10px"></div>
          <form action="" method="get" class="headers-mal-r-form form-before">
            <div class="input-group mb-3">
              <input type="text"  class="form-control" placeholder="请输入查询内容"   v-model="msg" aria-label="请输入查询内容" >
              <div class="input-group-append">
                <router-link v-model="msg" :to="{path:'/ssmv/',query:{form:msg}}">
                  <button class="btn btn-outline-secondary">
                    <Icon type="ios-search"/>
                  </button>
                </router-link>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import {ss} from "../../apis/apis";
  export default {
    name: "headers",
    data() {
      return {
        msg: '',

      }
    },
    components: {},
    methods: {
      // getdata() {
      //   ss(this.msg).then(res => {
      //     console.log(res.data)
      //     this.$store.commit('datatijiao',res.data)
      //   }).catch(err => {
      //     console.log(err)
      //   })
      // },

      getpath(msg) {
        console.log(msg);
        this.$router.push({
          path: `/ssmv/form=${msg}`
        })
      }
    },
    created() {
    }
  }
</script>

<style scoped lang="css">

  .headers{
    background-color: #fff0d6;
    margin-left: auto;
    margin-right: auto;
  }
  .headers-top{
    position: relative;
    z-index: 10;
    height: 40px;
    font-size: 12px;
    color: #f9f9f9;
    background: #1b1e21;
  }
  .headers-top-c:before{
    content: " ";
    display: table;
  }
  .headers-top-c:after{
    clear: both;
  }
  .headers-top-c:after{
    content: " ";
    display: table;
  }
  .headers-top-c{
    width: 1200px;
    margin-left: auto;
    margin-right: auto;
  }
  .headers-l{
    float: left;
    height: 40px;
    line-height: 40px;

  }
  .headers-wei:before{
    content: " ";
    display: table;
  }
  .headers-r{
    float: right;
    width: 120px;
    height: 40px;
    /*动画*/
    line-height: 40px;
    margin-left: 20px;
    text-align: center;
    background-color: #4a5462;
  }
  .headers-c{
    position: relative;
    float: right;
    height: 40px;
    line-height: 40px;
  }
  .headers-top a{
    color: #f9f9f9;
    font-size: 12px;
    line-height: 40px;
    display: inline-block;
  }
  a{
    /*background-color: white;*/
    text-decoration: none;
  }
  .headers-top-c .sap{
    margin: 0.3em;
    color: #1b1e21;
  }
  .sap-mass{
    padding: 0 10px;
  }

  .headers-mal{
    position: relative;
    z-index: 10;
    height: 100px;
  }
  .headers-mal-l{
    float: left;
    width: 60px;
    margin-top: 20px;
  }
  .logo{
    position: relative;
    display: block;
    width: 60px;
    height: 60px;
    overflow: hidden;
    background: violet;
  }
  .logo1{
    text-align: left;
    text-indent: -99em;
  }
  .logo:after{
    margin-left: -60px;
  }
  .headers-mal-c{
    float: left;
    width: 850px;
  }
  .headers-mal-c-ul{
    position: relative;
    z-index: 10;
    float: left;
    width: 1000px;
    height: 90px;
    margin: 0;
    padding: 10px 0 0 30px;
    list-style-type: none;
    font-size: 16px;

  }
  ul{
    display: block;
    list-style-type: disc;
    margin-block-start: 1em;
    margin-block-end: 1em;
    margin-inline-start: 0px;
    margin-inline-end: 0px;
    padding-inline-start: 40px;
  }
  .ul-before:before{
    content: " ";
    display: table;
  }
  .ul-before:after{
    clear: both;
  }
  .list-l{
    float: left;
  }
  .list-head{
    position: relative;
    float: left;
    width: 120px;
    padding-right: 15px;
  }
  li{
    display: list-item;
    text-align: -webkit-match-parent;
  }
  .link{
    display: block;
    padding: 25px 10px 40px;
    color: #1b1e21;
    transition: color .2s;
  }

  .headers-mal-r{
    float: right;
    width: 250px;
    margin-top: 25px;
  }
  form{
    display: block;
    margin-top: 0em;
  }
  .headers-mal-r-form{
    position: relative;
    width: 250px;
    height: 50px;
    z-index: 10;
  }
  .form-before:before{
    content: " ";
    display: table;
  }

  label{
    cursor: default;
  }


</style>

