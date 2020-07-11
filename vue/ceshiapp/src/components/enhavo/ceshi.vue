<template>
  <div class="container" style="background-color: #f9f9f9">
    <lunbo></lunbo>
    <div class="row">
      <div class="myui-panel myui-panel-bg clearfix" style="margin-top: 5px">
        <div class="myui-panel-box clearfix">
          <div class="myui-panel_head clearfix">
            <h3 class="title">电影</h3>
            <router-link to="/ceshi" class="more text-muted pull-right one-pan-link-mark">更多
              <Icon type="ios-arrow-forward"/>
            </router-link>
          </div>
        </div>
      </div>
    </div>
    <morenlist></morenlist>
    <div class="row">
      <div class="myui-panel myui-panel-bg clearfix" style="margin-top: 5px">
        <div class="myui-panel-box clearfix">
          <div class="myui-panel_head clearfix">
            <h3 class="title">电视剧</h3>
            <router-link to="#" class="more text-muted pull-right one-pan-link-mark">更多
              <Icon type="ios-arrow-forward"/>
            </router-link>
          </div>
        </div>
      </div>
    </div>
    <dsjmr></dsjmr>
    <div class="row">
      <div class="myui-panel myui-panel-bg clearfix" style="margin-top: 5px">
        <div class="myui-panel-box clearfix">
          <div class="myui-panel_head clearfix">
            <h3 class="title">综艺</h3>
            <router-link to="#" class="more text-muted pull-right one-pan-link-mark">更多
              <Icon type="ios-arrow-forward"/>
            </router-link>
          </div>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="myui-panel myui-panel-bg clearfix" style="margin-top: 5px">
        <div class="myui-panel-box clearfix">
          <div class="myui-panel_head clearfix">
            <h3 class="title">动漫</h3>
            <router-link to="#" class="more text-muted pull-right one-pan-link-mark">更多
              <Icon type="ios-arrow-forward"/>
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </div>

</template>

<script>
import lunbo from "./lunbo/lunbo";
import morenlist from "./dy/morenlist/morenlist";
import dsjmr from "./dxj/dsjmr/dsjmr";

  export default {
  name: "ceshi",
  components: {
    morenlist,
    lunbo,
    dsjmr,

  }
}
</script>

<style scoped lang="css">
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

  p {
    display: block;
    margin-block-start: 1em;
    margin-block-end: 1em;
    margin-inline-start: 0px;
    margin-inline-end: 0px;
  }
  .row{
    border-radius: 5px;
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

  .pull-right {
    float: right;
  }

  .text-muted {
    color: #999395;
  }

  .pull-right {
    float: right !important;
  }
  .fa {
    display: inline-block;
    font: normal normal normal 14px/1 FontAwesone;
    font-size: inherit;
    text-rendering: auto;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
  }

  .fa-angle-right:before {
    content: "\f105";
  }

</style>
