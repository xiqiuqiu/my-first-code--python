# -*- coding: utf-8 -*-
'''
爬去最新电影排榜榜单
使用requests ---bs4线路
OS:WIN10
'''

import requests
import bs4




def get_html(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status
        #该网站采用gbk编码
        r.encoding = 'gbk'
        return r.text
    except:
        return "something wrong"
        
def get_content(url):
    html = get_html(url)
    soup = bs4.BeautifulSoup(html,'lxml')
    
    #找到电影排行榜的ul列表
    movies_list = soup.find('ul', class_='picList clearfix')
    movies = movies_list.find_all('li')
    
        
        
    for top in movies:
            #找到图片链接
            img_url=top.find('img')['src']
            
            name = top.find('span',class_='sTit').a.txt
            #这里是一个异常捕获，防止没有上映时间的出现
            try:
                time = top.find('span',class_='sIntro').txt
            except:
                time = "暂无上映时间"
                '''   
            #这里用bs4库迭代找出“pactor”的所有子孙节点，即每一位演员解决了名字分割的问题
            actors = top.find('p',class_='pActor')
            actor=''
            for act in actors.contents:
                actor = actor + act.string +''
                '''
                
            #这里用bs4库迭代找出“pACtor”的所有子孙节点，即每一位演员解决了名字分割的问题
            actors = top.find('p',class_='pActor')
            actor= ''
            for act in actors.contents:
                actor = actor + act.string +''
                
            #找到影片简介
            intro = top.find('p',class_='pTxt pIntroShow').text
            
            print("片名:{}\t{}\n{}\n{} \n \n".format(name,time,actor,intro))
            
            #让我们把图片下载下来
            with open(r'C:\Users\luxu\.spyder-py3\txt\dianying'+name+'.png','wb+') as f:
               #f.write(requests.get(img_url).content)
               f.write(requests.get("http:"+img_url.split("jpg")[-2]+"jpg").content)
               
def main():
    url = 'http://dianying.2345.com/top/'
    get_content(url)
    
if __name__=="__main__":
    main()
    
    
            
    