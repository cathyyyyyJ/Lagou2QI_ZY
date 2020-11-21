import requests

class TestWeworkAccess:
    s=requests.Session()
    def test_get_token(self):
        params={
            "corpid": "ww76c279f05645c74e",
            "corpsecret": "1clN_YB1ht71CUbyJhzVqqxJWLCSEOoi_D8uhT0hfYI"
        }
        #说明：corpid可在我的企业中查看到。corpsecret可在管理工具的通讯录中查看#
        res = self.s.get(url="https://qyapi.weixin.qq.com/cgi-bin/gettoken",params=params)
        self.s.params={"access_token":res.json()['access_token']}
        try:
            return self.s.params['access_token']
        except Exception as e:
            raise ValueError("requests token error")

    #创建成员#
    def test_add(self):
        data={
                "userid": "zhangsan",
                "name": "张三",
                "alias": "jackzhang",
                "mobile": "13800000000",
                "department": [1]
        }
        #url可在企业微信API文档中查看#
        res_add=self.s.post("https://qyapi.weixin.qq.com/cgi-bin/user/create",json=data)
        print(res_add.json())
    #获取成员#
    def test_get(self):
        params={
            "userid":"zhangsan"
        }
        res_get=self.s.get("https://qyapi.weixin.qq.com/cgi-bin/user/get",params=params)
        print(res_get.json())
    #更新成员#
    def test_update(self):
        data={
            "userid": "zhangsan",
            "name": "李四",
        }
        res_post=self.s.post("https://qyapi.weixin.qq.com/cgi-bin/user/update",json=data)
        print(res_post.json())

    #删除成员#
    def test_delete(self):
        params={
            "userid":"zhangsan"
        }
        res_delete=self.s.get("https://qyapi.weixin.qq.com/cgi-bin/user/delete",params=params)
        print(res_delete.json())