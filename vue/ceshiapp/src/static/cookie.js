const cookie={
  setcookie(name,values,expiredays){
    const exdata=new Date();
    exdata.setTime(exdata.getTime()+expiredays);
    exdata.setDate(exdata.getDate()+expiredays);
    document.cookie=name+'='+escape(values) + ((expiredays == null) ? '' :';expires='+ exdata.toGMTString());
  },
  getCookie(name){
    let arr,reg =new RegExp("(^| )" + name + "=([^;]*)(;|$)");
    if(arr=document.cookie.match(reg)) {
      return arr[2];
    }
    else {
      return null
    }
  },
  delCookie(name){
    const exp = new Date();
    exp.setTime(exp.getTime() - 1);
    const cval = cookie.getCookie(name);
    if (cval != null) {
      document.cookie = name + '=; expires=Thu, 01 Jan 1970 00:00:01 GMT;';
    }
  }
}


export default cookie;

