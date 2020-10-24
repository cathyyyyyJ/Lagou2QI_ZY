import pytest
import yaml
from appium import webdriver


@pytest.mark.parametrize(["username","gender","phonenum"],yaml.safe_load(open("E:\project\pycharm\TASK\pythoncode7\members.yml",encoding='utf-8')))
class TestWechat:
    def setup(self):
        print("开始添加联系人")
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
        print("联系人添加成功")
    def test_add_member(self,username,gender,phonenum):
        print(f"{username}+{gender}+{phonenum}")
        #1-点击通讯录#
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='通讯录']").click()

        #2-滚动查找，点击添加成员#
        self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("添加成员").instance(0))').click()

        #3-点击手动输入添加#
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='手动输入添加']").click()

        self.driver.find_element_by_xpath("//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys(username)
        self.driver.find_element_by_xpath("//*[contains(@text,'手机')]/../android.widget.EditText").send_keys(phonenum)
        self.driver.find_element_by_xpath("//*[contains(@text,'性别')]/../android.widget.RelativeLayout").click()

        if gender == '女':
            self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.RelativeLayout").click()

        else:
            #为了区分界面上的男与弹出界面的男，当联系人性别为男时，先选女，再选男#
            el2 = self.driver.find_element_by_xpath(
                "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.RelativeLayout")
            el2.click()

            el3 = self.driver.find_element_by_xpath(
                "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.RelativeLayout")
            el3.click()

            el4 = self.driver.find_element_by_xpath(
                "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.RelativeLayout")
            el4.click()
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='保存']").click()
        #断言#
        text_assert=self.driver.find_element_by_xpath("//android.widget.TextView[@text='从微信/手机通讯录中添加']").text
        toasttest=self.driver.find_element_by_xpath("//*[@class='android.widget.Toast']")
        # assert toasttest == '添加成功'
        assert '从微信/手机通讯录中添加'== text_assert







