import re

import pytest
from requests import Session

from pythoncode10.api.access import Access
from pythoncode10.api.create_user import create_muti_data
from pythoncode10.api.wework import WeWork


class TestAccess:
    @pytest.fixture(scope="session")
    def token(self):
        return WeWork().test_get_token()
    def setup(self):
        self.access=Access()
    @pytest.mark.parametrize("userid,name,mobile", create_muti_data())
    def test_all(self,userid,name,mobile,token):
        try:
        #创建一个成员，对结果断言
            assert "created"==self.access.test_add(userid,name,mobile,token)['errmsg']
        except AssertionError as e:
            if "userid existed" in e.__str__():
                self.access.test_delete(userid, name, mobile, token)
            if "mobile existed" in e.__str__():
                delete_userid=re.findall(":(.*)‘$",e.__str__()) #借助正则表达式，冒号后面紧跟的字符为userid
                self.access.test_delete(userid, name, mobile, token)
                assert "created" == self.access.test_add(userid, name, mobile, token)['errmsg']
        #查询成员信息，对结果断言
        assert name==self.access.test_get(userid, name, mobile, token)['name']
        #更新一个成员#
        assert "updated"==self.access.test_update(userid,name="wangwu", mobile=mobile,token=token)['errmsg']
        assert "wangwu"==self.access.test_get(userid, name, mobile, token)['name']
        assert "deleted"==self.access.test_delete(userid, name, mobile, token)['errmsg']
        assert 60111==self.access.test_get(userid, name, mobile, token)['errcode']

    def test_session(self,token):
        s= Session()
        s.params ={"access_token":token}
        data={
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/get",
            "params": {
                "userid": "zhangsan1"
            }
        }
        print(s.request(**data))