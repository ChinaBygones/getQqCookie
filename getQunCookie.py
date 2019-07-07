from selenium import webdriver
import time


qq = input("请输入QQ:")
password = input("请输入密码:")
if(len(qq) == 0 or len(password) == 0):
    print("未输入QQ或者密码")
    exit();
def getQunCookie(qq,password):
    opt = webdriver.ChromeOptions()
    opt.add_argument('--headless')
    opt.add_argument('--no-sandbox')
    browser = webdriver.Chrome(chrome_options=opt)
    browser.get('https://xui.ptlogin2.qq.com/cgi-bin/xlogin?pt_disable_pwd=1&appid=715030901&daid=73&pt_no_auth=1&s_url=https%3A%2F%2Fqun.qq.com%2F')
    js = "document.getElementById('switcher_plogin').style.display='block';"
    browser.execute_script(js)
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
response = getQunCookie(qq,password)
print(response)