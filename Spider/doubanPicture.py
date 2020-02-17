import requests
import json
from lxml import html as ht
from selenium import webdriver

query = '宫崎骏'
header = {
    "Host": "www.douban.com",
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cookie": "_vwo_uuid_v2=DE81BD2137D14D63DD42F3DDA8A5985E8|15a55c5fefbfcb39af21944efc459ce3; douban-fav-remind=1; _ga=GA1.2.410204347.15382292",

}


# 下载图片
def download(src, id):
    dir = './' + str(id) + '.webp'
    try:
        pic = requests.get(src, timeout=10)
        fp = open(dir, 'wb')
        fp.write(pic.content)
        fp.close()
    except requests.exceptions.ConnectionError:
        print('图片无法下载')

'''
# json方式
for i in range(0, 41081, 20):
    url = 'https://www.douban.com/j/search_photo?q=' + query + '&limit=20&start=' + str(i)
    html = requests.get(url, headers=header).text
    response = json.loads(html, encoding='utf-8')
    for image in response['images']:
        print(image['src'])
        download(image['src'], image['id'])
'''

# xpath方式
url = "https://search.douban.com/movie/subject_search?search_text=%E5%AE%AB%E5%B4%8E%E9%AA%8F&cat=1002"
etree = ht.etree
# driver = webdriver.Chrome('../chromedriver/chromedriver') # linux
driver = webdriver.Chrome('../chromedriver/chromedriver.exe')   # windows
driver.get(url)
html = etree.HTML(driver.page_source)
src_xpath = "//div[@class='item-root']/a[@class='cover-link']/img[@class='cover']/@src"
title_path = "//div[@class='item-root']/div[@class='detail']/div[@class='title']/a[@class='title-text']"
srcs = html.xpath(src_xpath)
titles = html.xpath(title_path)
for src, title in zip(srcs, titles):
    download(src, title.text)
