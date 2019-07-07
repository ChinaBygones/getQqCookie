# coding:utf-8
#Author Bygones
#QQ 1533102269


from selenium import webdriver
import time

import socket
from furl import furl
import re
from selenium import webdriver
import time
from multiprocessing import Process


def getQzoneCookie(qq,password):
    opt = webdriver.ChromeOptions()
    opt.add_argument('--headless')
    opt.add_argument('--no-sandbox')
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
    return 'Cookie:' + i
def handle_client(client_socket):
    """
    处理客户端请求
    """
    request_data = client_socket.recv(1024)
    request_lines = request_data.splitlines()
    request_start_line = request_lines[0]
    f = furl(request_start_line)
    if (bool(1 - f.args.has_key("qq")) or bool(1 - f.args.has_key("password"))):
        return "字段key不存在";
    qq = f.args["qq"]
    password = f.args["password"]
    password = password.replace(" HTTP/1.1'", '')
    # 构造响应数据
    response_start_line = "HTTP/1.1 200 OK\r\n"
    response_headers = "Server: My server\r\n"
    response_body = getQzoneCookie(qq,password)
    response = response_start_line + response_headers + "\r\n" + response_body

    # 向客户端返回响应数据
    client_socket.send(bytes(response, "utf-8"))

    # 关闭客户端连接
    client_socket.close()


if __name__ == "__main__":
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("", 9501))
    server_socket.listen(128)

    while True:
        client_socket, client_address = server_socket.accept()
        print("[%s, %s]用户连接上了" % client_address)
        handle_client_process = Process(target=handle_client, args=(client_socket,))
        handle_client_process.start()
        client_socket.close()
