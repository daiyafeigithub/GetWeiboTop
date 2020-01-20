import requests
from lxml import etree
import time
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
data = {
     'cate': 'realtimehot'
     }
def getweibo():
    r = requests.get('http://s.weibo.com/top/summary?1', params=data, headers=headers)
    print(r.url)
    html = r.text
    selector = etree.HTML(html)
    tr = selector.xpath("//div[@id='pl_top_realtimehot']/table/tbody/tr")
    del tr[0]
    strs=""
    for t in tr[:10]:
        id = eval(t.find(u".//td[@class='td-01 ranktop']").text)
        title = t.find(u".//td[@class='td-02']").find(u".//a").text
        num = eval(t.find(u".//td[@class='td-02']").find(u".//span").text)
        href=t.find(u".//td[@class='td-02']").find(u".//a").get('href')
        str0="### top" +str(id)+"   ["+title+"](http://s.weibo.com"+href +")"+"\n"+"热度:"+ str(num)
        strs=strs+"\n"+str0
    with open("D:\hexo\source\weibo\index.md", "w", encoding='utf-8') as f:
            f.write("---\ntitle: 微博百度\n---")
            f.write("\n---\n 微博热搜\n---")
            f.write("\n更新时间:" + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
            f.write(strs)
            f.write("\n")
#baidu

head = {}
url = "http://top.baidu.com/buzz?b=341&fr=topindex"
head["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:63.0) Gecko/20100101 Firefox/63.0"
head["Accept"]= "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
head["Accept-Language"]= "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2"
head["Connection"] = "keep-alive"
def getbaidu():
    print("百度热搜top10： ")
    res = requests.get(url , headers = head)
    with open("html.txt", "wb") as f:
        f.write(res.content)
    html = etree.parse('html.txt' , etree.HTMLParser(encoding='gbk'))
    top_list = html.xpath('//a[@class="list-title"]/text()')
    href=html.xpath('//a[@class="list-title"]//@href')
    num_search = html.xpath('//span[@class="icon-rise"]/text()')
    count=0
    strs = ""
    for i  , j,href in zip(top_list[:10] , num_search[:10],href[:10]):
        count+=1
        print(i ,"搜索指数为：" ,  j  )
        str0 = "### top" + str(count) + "   [" + i + "]("+href + " )" + "\n 热度:" + str(j)
        strs = strs + "\n" + str0
    with open("D:\hexo\source\/weibo\index.md", "a", encoding='utf-8') as f:
        f.write("\n---\n 百度热搜\n---")
        f.write("\n更新时间:"+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
        f.write(strs)
if  __name__ == '__main__':
     getweibo()
     getbaidu()




