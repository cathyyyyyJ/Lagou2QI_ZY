from pythoncode10.api.base_api import BaseApi


class Access(BaseApi):
    # 创建成员#
    def test_add(self, userid, name, mobile, token, depart=None):
        if depart is None:
            depart=[1]
        data = {
            "method":"post",
            "url":"https://qyapi.weixin.qq.com/cgi-bin/user/create",
            "params":{
                "access_token": token,
            },
            "json":{
                "userid": userid,
                "name": name,
                "mobile": mobile,
                "department": depart
            }
        }
        res_add = self.send_api(data)
        return res_add

    # 获取成员#
    def test_get(self, userid, name, mobile, token):
        data={
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/get",
            "params": {
                "access_token": token,
                "userid": userid
            },
            "json":{
                "name": name,
                "mobile": mobile,
            }
        }
        res_get =self.send_api(data)
        return res_get

    # 更新成员#
    def test_update(self,userid, name, mobile, token):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/update",
            "params":{
                "access_token":token
            },
            "json":{
                "userid": userid,
                "name": name,
                "mobile": mobile,
            }
        }
        res_update = self.send_api(data)
        return res_update

    # 删除成员#
    def test_delete(self,userid, name, mobile, token):
        data= {
            "method":"get",
            "url":"https://qyapi.weixin.qq.com/cgi-bin/user/delete",
            "params":{
                "access_token": token,
                "userid": userid
            },
            "json": {
                "name": name,
                "mobile": mobile,
            }

        }
        res_delete = self.send_api(data)
        return res_delete