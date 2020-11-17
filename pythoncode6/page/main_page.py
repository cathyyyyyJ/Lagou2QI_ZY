from selenium.webdriver.common.by import By
from pythoncode6.page.base_page import BasePage
from pythoncode6.page.del_member import DelMember
from pythoncode6.page.import_page import ImpMember


class MainPage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/loginpage_wx"
    def page_goto_del(self):
        self.WebwaitClick(By.XPATH, "//*[@id='menu_contacts']/span")
        self.find(By.XPATH,"//*[@id='menu_contacts']/span").click() #点击通讯录界面
        self.WebwaitVisible(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")#待通讯录界面成员加载完成
        return DelMember(self.driver)
    def page_goto_imp(self):
        self.WebwaitClick(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)")
        self.find(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)").click() #点击导入通讯录
        self.WebwaitClick(By.XPATH,".//*[@id='main']/div/div[2]/div[2]/div[1]/a/input")#显式等待，查看上传文件按钮是否可点击
        return ImpMember(self.driver)