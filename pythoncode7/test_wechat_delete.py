import pytest
import yaml
from appium import webdriver


@pytest.mark.parametrize(["username","gender","phonenum"],yaml.safe_load(open("E:\project\pycharm\TASK\pythoncode7\members.yml",encoding='utf-8')))
class TestWechat:
    def setup(self):
        print("开始删除联系人")
        desired_caps = {
            "deviceName": "127.0.0.1:7555",
            "platformName": "Android",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.LaunchSplashActivity",
            'automationName': "uiautomator2",
            "noReset": "true"
        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(30)
    def teardown(self):
        print("成功删除联系人")
    def test_del_member(self,username,gender,phonenum):
        #1-点击通讯录#
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='通讯录']").click()

        #2-滚动查找，点击要删除的成员姓名#
        self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("%s").instance(0))'% username).click()
        # 3-点击成员信息右上角的三个点#
        self.driver.find_element_by_id("com.tencent.wework:id/hxm").click()
        # 4-点击编辑成员#
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='编辑成员']").click()
        # 5-删除成员#
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='删除成员']").click()
        # 6-确认删除#
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='确定']").click()
        #断言#
        text_assert1=self.driver.find_element_by_xpath("//android.widget.TextView[@text='外部联系人']").text
        print(text_assert1)
        assert '外部联系人' == text_assert1








