from efficient_apriori import apriori
from lxml import etree
from selenium import webdriver
import csv
import time

driver = webdriver.Chrome('../chromedriver/chromedriver.exe')  # windows

director = '宁浩'
base_url = 'https://search.douban.com/movie/subject_search?search_text=' + director + '&cat=1002&start='
file_name = './' + director + '.csv'
out = open(file_name, 'w', newline='', encoding='utf-8-sig')
csv_write = csv.writer(out, dialect='excel')

flags = []


def download(request_url):
    driver.get(request_url)
    time.sleep(1)
    html = driver.find_element_by_xpath("//*").get_attribute("outerHTML")
    html = etree.HTML(html)

    movie_lists = html.xpath("/html/body/div[@id='wrapper']/div[@id='root']/div[1]//div[@class='item-root']/div[@class='detail']/div[@class='title']/a[@class='title-text']")
    movie_actors = html.xpath("/html/body/div[@id='wrapper']/div[@id='root']/div[1]//div[@class='item-root']/div[@class='detail']/div[@class='meta abstract_2']")

    num = len(movie_lists)
    if num > 15:
        movie_lists = movie_lists[1:]
        movie_actors = movie_actors[1:]

    for movie, actors_list in zip(movie_lists, movie_actors):
        if actors_list.text is None:
            continue
        print(actors_list.text)
        actors = actors_list.text.split('/')
        # 判断导演是否为指定的director
        if actors[0].strip() == director and movie.text not in flags:
            # 将第一个字段设置为电影名称
            actors[0] = movie.text
            flags.append(movie.text)
            csv_write.writerow(actors)

        print('OK')  # 代表这页数据下载成功
        print(num)
        if num >= 14:  # 有可能一页会有14个电影
            # 继续下一页
            return True
        else:
            # 没有下一页
            return False


# 开始的ID为0，每页增加15
start = 0
while start < 10000:  # 最多抽取1万部电影
    request_url = base_url + str(start)
    # 下载数据，并返回是否有下一页
    flag = download(request_url)
    if flag:
        start = start + 15
    else:
        break
out.close()
print('finished')


