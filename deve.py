# encoding=utf-8
import requests
import time

def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()#判断返回代码 若不为200 跳出异常
        r.encoding = r.apparent_encoding#通过分析得出编码
        return r.text
    except:
        return "产生异常"

if __name__ == "__main__":
    url = "https://www.baidu.com"
    bg_time = time.time()#获取开始时间
    for i in range(100):#循环100次
        answer = getHTMLText(url)
        if answer:
            print("正在爬取第{}次".format(i))
    end_time = time.time()#获取结束时间
    print("用时{:.2f}s".format(end_time - bg_time))
    print(answer)