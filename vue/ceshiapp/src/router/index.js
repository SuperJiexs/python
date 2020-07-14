import Vue from 'vue';
import Router from 'vue-router';
import index from "../components/index/index";
import morenlist from "../components/enhavo/dy/morenlist/morenlist";
import ceshilist from "../components/enhavo/dy/ceshilist/ceshilist";
import ssmv from "../components/enhavo/ssmv/ssmv";
import detail from "../components/enhavo/xiangqing/detail";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'index',
      component: index,
    },
    {
      path:'/ceshi',
      name: ceshilist,
      component: ceshilist,
    },
    {
      path:'/ssmv/',
      name: 'ssmv',
      component: ssmv,
    },
    {
      path:'/detail/',
      name: detail,
      component: detail,
    },

  ],
})
