from selenium.webdriver.common.by import By
from pythoncode6.page.base_page import BasePage


class DelMember(BasePage):
    def del_member(self,namelist):
        #找到需要删除的成员名称#
        self.find(By.XPATH,'//*[@title="test22"]/..').click() #找到要删除的成员，点击，进去详情页#
        self.WebwaitClick(By.CSS_SELECTOR,'.js_del_member') #待删除按钮加载完成#
        self.find(By.CSS_SELECTOR,'.js_del_member').click() #点击删除
        self.WebwaitClick(By.CSS_SELECTOR,'#__dialog__MNDialog__ > div > div.qui_dialog_foot.ww_dialog_foot > a.qui_btn.ww_btn.ww_btn_Blue')
        self.find(By.CSS_SELECTOR, '#__dialog__MNDialog__ > div > div.qui_dialog_foot.ww_dialog_foot > a.qui_btn.ww_btn.ww_btn_Blue').click()#点击所有成员
        self.WebwaitVisible(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)") #待通讯录成员加载完成（全部显示）
        #获得通讯录中所有的成员名称，放在 namelist中#
        elements = self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        print(elements)
        for element in elements:
            a=element.get_attribute("title")
            namelist.append(a)
        return namelist
