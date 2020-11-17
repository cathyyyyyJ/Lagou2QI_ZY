from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    _base_url = ""
    def __init__(self,driver_basepage:WebDriver = None):
        if driver_basepage == None:
            option = Options()
            option.debugger_address = "localhost:9222"
            self.driver = webdriver.Chrome(options=option)
        else:
            self.driver = driver_basepage
        if self._base_url != "":
            self.driver.get(self._base_url)
    def find(self,by,value): #查找单个元素
        return self.driver.find_element(by=by, value=value)
    def finds(self,by,value):#查找多个元素
        return self.driver.find_elements(by=by, value=value)
    def WebwaitClick(self,by,value):  #设置显式等待，元素是否可点击
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((by,value)))
    def WebwaitVisible(self, by, value): #设置显式等待，元素是否显示
        return WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((by,value)))
    def quit(self):
        return self.driver.quit()
