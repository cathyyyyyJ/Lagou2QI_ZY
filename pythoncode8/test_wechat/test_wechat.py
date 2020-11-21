import pytest
import yaml

from pythoncode8.page.app import App

namelist=[]
@pytest.mark.parametrize(['username', 'gender', 'phonenum'], yaml.safe_load(
    open("E:/project/pycharm/TASK/pythoncode8/data/members.yml", encoding='utf-8')))
class TestWechat:
    def setup(self):
        self.app=App()
    #1-添加成员#
    def test_add_mem(self,username,gender,phonenum):
        toasttext=self.app.start().main().page_add().add_member(username,gender,phonenum)
        assert toasttext == '添加成功'
    #2-删除成员#
    def test_del_mem(self,username,gender,phonenum):
        #删除指定成员，同时获取通讯录页面上的文本信息，其中包含通讯录信息
        namelist=self.app.start().main().page_del().del_member(username)
        #判断通讯录中是否有删除的成员
        assert username not in namelist