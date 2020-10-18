import json
import time
from selenium import webdriver


class Testcookie:
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
    # #获取cookie，只需要执行一次即可，直到cookie过期，过期后需要获取新的cookie
    # def test_get_cookie(self):
    #     time.sleep(15)
    #     cookies = self.driver.get_cookies()
    #     with open("E:/project/pycharm/TASK/pythoncode5/test_login/cookie.json","w") as f:  #将cookie信息写入json文件中#
    #         json.dump(cookies,f)
    def test_cookie_login(self):
        cookies = json.load(open("E:/project/pycharm/TASK/pythoncode5/test_login/cookie.json"))
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        time.sleep(20)
        self.driver.refresh()

