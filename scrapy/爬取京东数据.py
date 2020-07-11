import urllib.request,urllib.parse
import json
# 引入标注库
from lxml import html
# 爬虫基本对象
class pachong(object):
    url = "https://search.jd.com/Search?"
    # 引入网页的请求头文件 反扒措施
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10"
    }
    #
    def __init__(self,name,startpage,endpage,):
        self.name=name
        self.startpage=startpage
        self.endpage=endpage
        self.kw={}
    def handler(self,page):
        data={
            "keyword": self.name,
            "enc": "utf-8",
            "qrst":"1",
            "rt":"1",
            "stop":"1",
            "wp":self.name,
            "page":page,
            "s":"1",
            "click":"0"
        }
        # 将data中的数据封装到url路由中
        url_now=self.url+urllib.parse.urlencode(data)
        # 爬取页面
        req=urllib.request.Request(url_now,headers=self.headers)
        return req
    def jiexi(self,html_data):
        # 对Element对象使用xpath筛选，返回一个列表（里面的元素也是Element）
        li_list=html_data.xpath('//div[@class="goods-list-v2 gl-type-3 J-goods-list"]/ul[@class="gl-warp clearfix"]/li')
        for i in li_list:
            spmc="".join(i.xpath('./div/div[@class="p-name p-name-type-2"]/a/em/text()'))
            # splj="http:%s"%(i.xpath('./div/div[@class="p-img"]/a[@target="_blank"]/@href').get())
            # sptp="http:%s"%(i.xpath('//*[@id="J_goodsList"]/ul/li[1]/div/div[1]/a/img/@source-data-lazy-img').get())
            spdp="".join(i.xpath('./div/div[@class="p-shop"]/span/a/text()'))
            spjg = "".join(i.xpath('./div/div[@class="p-price"]/strong/i/text()'))
            self.kw = {
                "商品名称": spmc,
                "商品价格": spjg,
                # "商品图片链接": sptp,
                # "商品链接": splj,
                "商品店铺名称": spdp
            }
            print(self.kw)
            # json_str=json.dumps(self.kw)
            # with open('./jd.json','w')as json_file:
            #     json_file.write(json_str)
    def run(self):
        for page in range(self.startpage,self.endpage+1):
            # 代理访问
            opener=urllib.request.build_opener(urllib.request.HTTPHandler)
            # 对html文本使用 etree.HTML(html)解析，得到Element对象
            html_data=html.etree.HTML(opener.open(self.handler(page=(1+2*(page-1)))).read())
            self.jiexi(html_data)
def main():
    name=input("输入要搜索的关键字：")
    startpage=int(input("请输入起始页码："))
    endpage=int(input("请输入终止页码："))
    # 实例化对象
    sprit=pachong(name,startpage,endpage)
    # 调用方法
    sprit.run()

if __name__ == '__main__':
    main()