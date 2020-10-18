#浏览器复用登录企业微信#
""""
1、配置环境变量：右键chrome浏览器，在属性中查看路径，添加到path环境变量中
2、命令行输入启动命令：chrome --remote-debugging-port=9222(端口自定义)
3、浏览器中输入http://localhost:9222/检查是否配置成功
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Testlogin:
    def test_weblogin(self):
        option=Options()
        option.debugger_address="localhost:9222"
        driver=webdriver.Chrome(options=option)
        driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")

