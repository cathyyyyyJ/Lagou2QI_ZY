import requests

from pythoncode10.api.base_api import BaseApi


class WeWork(BaseApi):
    def test_get_token(self):
        data={
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params":{
                "corpid": "ww76c279f05645c74e",
                "corpsecret": "1clN_YB1ht71CUbyJhzVqqxJWLCSEOoi_D8uhT0hfYI"
            }
        }
        #说明：corpid可在我的企业中查看到。corpsecret可在管理工具的通讯录中查看#
        res=requests.request(**data).json()
        try:
            return res['access_token']
        except Exception as e:
            raise ValueError("requests token error")