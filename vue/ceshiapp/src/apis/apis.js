import axios from 'axios';

let host_ct = '/ct';
let host_cl = '/cl';
let  host_ad='/ad';

//城市
export const citys = params => {
  return axios.get(`${host_ct}/citys/`)
}

//ceshi
export const cl = params => {
  return axios.get(`${host_cl}/mua/`)
}

//电影列表

export const dys = params => {
  return axios.get(`${host_ct}/dys/`)
}

//搜索功能

export const ss = ssnm => {
  return axios.get(`${host_ct}/dy/${ssnm}`+'/')
}


//详情页
export const xq = mdy => {
  return axios.get(`${host_ct}/mdy/${mdy}`+'/')
}


//热门电影

export const mvrm = params => {
  return axios.get(`${host_ct}/mvrm/`)
}

//denglu
export const denglu = params => {
  return axios.post(`${host_cl}/mua/`,params)
}











