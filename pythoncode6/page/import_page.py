from selenium.webdriver.common.by import By
from pythoncode6.page.base_page import BasePage


class ImpMember(BasePage):
    def imp_member(self,namelist):
        self.find(By.XPATH,"//*[@id='main']/div/div[2]/div[2]/div[1]/a/input").send_keys("E:/project/pycharm/TASK/pythoncode6/page/addressbook2.xls")
        self.find(By.CSS_SELECTOR, ".ww_fileImporter_submit").click()  #点击导入
        self.WebwaitClick(By.CSS_SELECTOR,".ww_fileImporter_successBtnWrap")#等待导入完成#
        self.find(By.CSS_SELECTOR,".ww_btn_Back").click() #点击返回，到通讯录页面中#
        self.WebwaitVisible(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)") #待成员加载完成
        #获得通讯录中所有的成员名称，放在 namelist中#
        elements = self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        for element in elements:
            a=element.get_attribute("title")
            namelist.append(a)
        return namelist