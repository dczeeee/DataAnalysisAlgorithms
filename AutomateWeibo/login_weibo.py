from selenium import webdriver
import time

browser = webdriver.Chrome('../chromedriver/chromedriver.exe')  # windows


# 登录微博
def weibo_login(username, password):
    # 打开微博登录页
    browser.get('https://passport.weibo.cn/signin/login')
    browser.implicitly_wait(5)
    time.sleep(1)
    # 填写登录信息
    browser.find_element_by_id("loginName").send_keys(username)
    browser.find_element_by_id("loginPassword").send_keys(password)
    time.sleep(1)
    # 点击登录
    browser.find_element_by_id("loginAction").click()
    time.sleep(1)


username = '13610655553'
password = 'haoyu13610655553'
weibo_login(username, password)







