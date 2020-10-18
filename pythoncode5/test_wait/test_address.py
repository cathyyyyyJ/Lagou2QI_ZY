import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Testcookie:
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")

    def test_cookie_login(self):
        cookies = json.load(open("E:/project/pycharm/TASK/pythoncode5/test_login/cookie.json"))
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        while True:
            self.driver.refresh()
            res = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable
                                                       ((By.ID, "menu_index")))
            if res is not None:
                break
        # self.driver.refresh()
        WebDriverWait(self.driver,10).until(expected_conditions.
                                            element_to_be_clickable((By.CSS_SELECTOR,".index_service_cnt_itemWrap:nth-child(2)")))
        self.driver.find_element(By.CSS_SELECTOR,".index_service_cnt_itemWrap:nth-child(2)").click()
        WebDriverWait(self.driver,10).until(expected_conditions.
                                            presence_of_element_located((By.XPATH,"//*[@id='main']/div/div[2]/div[2]/div[1]/a/input")))

        self.driver.find_element(By.XPATH,"//*[@id='main']/div/div[2]/div[2]/div[1]/a/input").send_keys("E:/project/pycharm/PYCharmWeb自动化/demo/ShiZhanZY/SZ1/data/workbook.xls")
        WebDriverWait(self.driver, 10).until(expected_conditions.
                                             presence_of_element_located((By.XPATH,"//*[@id='main']/div/div[2]/div[2]/div[1]/a/input")))
        assert_ele=self.driver.find_element(By.XPATH,"//*[@id='main']/div/div[2]/div[2]/div[1]/div[2]").text
        print(assert_ele)
        assert assert_ele=="workbook.xls"




