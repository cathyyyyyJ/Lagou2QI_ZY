import time

from pythoncode8.page.base_page import BasePage

namelist=[]
class DelMember(BasePage):
    def del_member(self,username):
        # 1-点击通讯录#
        self.find_xp("//android.widget.TextView[@text='通讯录']").click()
        # 2-滚动查找，点击要删除的成员姓名#
        self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("%s").instance(0))' % username).click()
        # 3-点击成员信息右上角的三个点#
        self.find_id("com.tencent.wework:id/hxm").click()
        # 4-点击编辑成员#
        self.find_xp("//android.widget.TextView[@text='编辑成员']").click()
        # 5-删除成员#
        self.find_xp("//android.widget.TextView[@text='删除成员']").click()
        # 6-确认删除#
        self.find_xp("//android.widget.TextView[@text='确定']").click()
        time.sleep(10) #强制等待#
        #7-获取列表中的文本信息，包含通讯录内成员名称#
        # elements=self.driver.find_elements_by_xpath("//*[@resource-id='com.tencent.wework:id/ecj']//*[@class='android.widget.TextView']")
        elements=self.finds_xp("//*[@resource-id='com.tencent.wework:id/ecj']//*[@class='android.widget.TextView']")
        for i in elements:
            namelist.append(i.text)
        return namelist