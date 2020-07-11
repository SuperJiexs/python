<template>
  <div>
    <div class="tos-top">
      <div class="tos-top-c be">
        <div class="tos-top-c-s">
          <ul class="tos-top-c-s-ul be">
            <li v-for="data in datalist" :key="data">
              <a href="#">
                <em class="tos-top-c-em-">
                  {{data}}
                </em>
              </a>
            </li>
          </ul>
        </div>
        <div class="tos-top-c-f be">
          <dl class="tos-top-c-dl tos-top-c-dl-f">
            <dt>帮助</dt>
            <dd v-for="dd in datadd1" :key="dd">
              <a href="#">{{ dd }}</a>
            </dd>
          </dl>
          <dl class="tos-top-c-dl">
            <dt>售后</dt>
            <dd v-for="dd in datadd2" :key="dd">
              <a href="#">{{ dd }}</a>
            </dd>
          </dl>
          <dl class="tos-top-c-dl">
            <dt>店铺</dt>
            <dd v-for="dd in datadd3" :key="dd">
              <a href="#">{{ dd }}</a>
            </dd>
          </dl>
          <dl class="tos-top-c-dl">
            <dt>简介</dt>
            <dd v-for="dd in datadd4" :key="dd">
              <a href="#">{{ dd }}</a>
            </dd>
          </dl>
          <dl class="tos-top-c-dl">
            <dt>关注</dt>
            <dd v-for="dd in datadd5" :key="dd">
              <a href="#">{{ dd }}</a>
            </dd>
          </dl>
          <dl class="tos-top-c-dl">
            <dt>服务</dt>
            <dd v-for="dd in datadd6" :key="dd">
              <a href="#">{{ dd }}</a>
            </dd>
          </dl>
          <div class="tos-top-c-div">
            <p>电话</p>
            <p>13931909312</p>
            <p>qq</p>
            <p>572607562</p>
            <p>微信</p>
            <p>zxj572607562</p>
          </div>
        </div>
      </div>
    </div>
    <div class="tos-mal">
      <div class="tos-mal-m ir">
        <p>
          自己配置玩一玩
        </p>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: "tosto",
    data(){
      return{
        datalist:["维修服务","退货服务","换货服务","包邮服务","主页网站"],
        datadd1:['账户管理','购物指南','操作指南'],
        datadd2:["售后客服","服务内容","资料下载"],
        datadd3:["暂无店铺"],
        datadd4:["了解网站"],
        datadd5:["qq","微信"],
        datadd6:["暂无服务"],

      }
    },
  }
</script>

<style scoped lang="css">
  p{
    display: block;
    margin-block-start: 1em;
    margin-block-end: 1em;
    margin-inline-start: 0px;
    margin-inline-end: 0px;
    margin: 0 0 5px 0;
  }
  dd{
    margin: 10px 0 0;
    font-size: 12px;
    display: block;
    text-align: center;
  }
  dt{
    margin: -1px 0 26px;
    font-size: 14px;
    line-height: 1.25;
    color: #424242;
    text-align: center;
  }
  dl{
    display: block;
    margin-block-start: 1em;
    margin-block-end: 1em;
    margin-inline-start: 0px;
    margin-inline-end: 0px;
  }
  .tos-top{
    width: 1226px;
    margin-left: auto;
    margin-right: auto;
  }
  em{
    font-style:italic;
  }
  div{
    display: block;
  }
  .tos-mal{
    padding: 30px 0;
    font-size: 12px;
    background-color: #e2e6ea;
  }
  .tos-mal-m{
    clear: both;
    width: 100%;
    height: 20px;
    margin: 30px auto 0;;
  }
  .ir{
    display: block;
    text-align: center;

    overflow: hidden;
  }
  .be:before{
    content: " ";
    display: table;
  }
  .be:after{
    clear: both;
  }
  .be:after{
    content: " ";
    display: table;
  }
  .tos-top-c{
    width: 1200px;
    margin-left: auto;
    margin-right: auto;
  }
  .tos-top-c-s{
    padding: 30px 0;
    border-bottom: 1px solid #e8e8e8;
  }
  .tos-top-c-s-ul{
    margin: 0;
    padding: 0;
    list-style-type: none;
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

  a{
    text-decoration: none;
    background-color: white;
  }
  a:-webkit-any-link{
    color: -webkit-link;
    cursor: pointer;
    text-decoration: none;
  }
  li{
    float: left;
    width: 19.8%;
    height: 25px;
    border-left: 1px solid #e6e6e6;
    font-size: 16px;
    line-height: 25px;
    text-align: center;
  }
  .tos-top-c-f{
    padding: 40px 0;
  }
  .tos-top-c-f:before{
  }
  li:first-child{
    border-left: none;
  }
  .tos-top-c-dl{
    float: left;
    width: 153px;
    height: 100px;
    margin: 0;
  }
  .tos-top-c-div{
    float: right;
    width: 250px;
    border-left: 1px solid #e2e3e5;
    text-align: center;
    color: #4a5462;
  }


</style>
