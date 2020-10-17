import pytest
import yaml

from pythoncode4.cal import calculator


def test_env(cmdoption):
    print(f"{cmdoption}")


@pytest.mark.parametrize(["a","b"],
                             yaml.safe_load(open("E:/project/pycharm/PYCharm测试报告定制/pythoncode4/caldata.yml")))



class Test_cal:
    def setup(self):
        print("------开始计算------")

    def teardown(self):
        print("------计算结束------")



    @pytest.mark.run(order=1)
    @pytest.mark.dependency(name='addtest') #依赖关系：减法依赖加法，除法依赖乘法
    def test_add(self,a,b):
        print("测试 加法")
        print(f"{a}+{b}={calculator(a,b).add_ca()}")

    @pytest.mark.run(order=3)
    @pytest.mark.dependency(name='multest') #依赖关系：减法依赖加法，除法依赖乘法
    def test_mul(self, a, b):
        print("测试 乘法")
        print(f"{a}*{b}={calculator(a, b).mul_ca()}")

    @pytest.mark.run(order=4)
    @pytest.mark.dependency(depends=['multest']) #依赖关系：减法依赖加法，除法依赖乘法
    def test_div(self, a, b):
        print("测试 除法")
        print(f"{a}/{b}={calculator(a, b).div_ca()}")

    @pytest.mark.run(order=2)
    @pytest.mark.dependency(depends=['addtest']) #依赖关系：减法依赖加法，除法依赖乘法
    def check_sub(self, a, b):
        print("测试 减法")
        print(f"{a}-{b}={calculator(a, b).sub_ca()}")
