
#用于app常用的操作：启动、关闭、重启、进入主页面
from appium import webdriver
from appium.webdriver.webdriver import WebDriver

from pythoncode8.page.base_page import BasePage
from pythoncode8.page.main_page import MainPage


class App(BasePage):
    driver:WebDriver
    def start(self):
        if self.driver == None:
            desired_caps = {
            "deviceName": "127.0.0.1:7555",
            "platformName": "Android",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.LaunchSplashActivity",
            'automationName': "uiautomator2",
            "noReset": "true"
            }
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        else:
            self.driver.launch_app()
        self.driver.implicitly_wait(40)
        return self
    def main(self): #进入到主页
        return MainPage(self.driver)
