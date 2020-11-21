from appium.webdriver.common.mobileby import MobileBy

from pythoncode8.page.base_page import BasePage


class AddMember(BasePage):
    def add_member(self,username,gender,phonenum):
        # 1-点击通讯录#
        self.find_xp("//android.widget.TextView[@text='通讯录']").click()
        # 2-滚动查找，点击添加成员#
        self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("添加成员").instance(0))').click()
        # 3-点击手动输入添加#
        self.find_xp("//android.widget.TextView[@text='手动输入添加']").click()
        self.find_xp("//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys(username)
        self.find_xp("//*[contains(@text,'手机')]/../android.widget.EditText").send_keys(phonenum)
        self.find_xp("//*[contains(@text,'性别')]/../android.widget.RelativeLayout").click()
        # 4-性别默认为男，无论要添加的成员性别为男还是女，都需要点击性别列进行选择，否则保存按钮不可点击#
        if gender == '女':
            self.find_xp(
                "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.RelativeLayout").click()
        else:
            # 为了区分界面上的男与弹出界面的男，当联系人性别为男时，先选女，再选男#
            el2 = self.find_xp(
                "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.RelativeLayout")
            el2.click()

            el3 = self.find_xp(
                "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.RelativeLayout")
            el3.click()

            el4 = self.find_xp(
                "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.RelativeLayout")
            el4.click()
        self.find_xp("//android.widget.TextView[@text='保存']").click()
        # 5-获取添加成功后的toast,以便进行断言#
        return self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text