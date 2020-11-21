from appium.webdriver.webdriver import WebDriver



class BasePage:
    driver:WebDriver
    def __init__(self,driver:WebDriver = None):
        self.driver = driver
    def find_xp(self,xpath):
        return self.driver.find_element_by_xpath(xpath=xpath)
    def finds_xp(self,xpath):
        return self.driver.find_elements_by_xpath(xpath=xpath)
    def find_id(self,id_):
        return self.driver.find_element_by_id(id_=id_)
    def quit(self):
        return self.driver.quit()