from selenium import webdriver
import time
qq = input("请输入QQ:")
password = input("请输入密码:")
if(len(qq) == 0 or len(password) == 0):
    print("未输入QQ或者密码")
    exit();
def getQzoneCookie(qq,password):
    opt = webdriver.ChromeOptions()
    opt.add_argument('--headless')
    browser = webdriver.Chrome(chrome_options=opt)
    browser.get('http://qzone.qq.com')
    browser.switch_to_frame('login_frame')
    browser.find_element_by_id('switcher_plogin').click()
    browser.find_element_by_id('u').send_keys(qq)
    browser.find_element_by_id('p').send_keys(password)
    browser.find_element_by_id("login_button").click()
    time.sleep(1)
    cookie = browser.get_cookies()
    cookie_dict = []
    for c in cookie:
        ck = "{0}={1};".format(c['name'], c['value'])
        cookie_dict.append(ck)
    i = ''
    for c in cookie_dict:
        i += c
    browser.quit()
    return 'Cookie:'+i
response = getQzoneCookie(qq,password)
print (response)