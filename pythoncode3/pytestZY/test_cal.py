import pytest
import yaml

from pythoncode3.pytestZY.cal import Calculator


@pytest.mark.parametrize(["a", "b"],
                         yaml.safe_load(open("E:/project/pycharm/PYCharmHZZY/pytestdemo/testcal/testdata.yml")))
class TestCal:
    def test_add(self, a, b, setUp):
        print("测试 加法")
        print(f"{a}+{b}={Calculator().add(a, b)}")

    def test_sub(self, a, b, setUp):
        print("测试 减法")
        print(f"{a}-{b}={Calculator().sub(a, b)}")

    def test_mul(self, a, b, setUp):
        print("测试 乘法")
        print(f"{a}*{b}={Calculator().mul(a, b)}")

    def test_div(self, a, b, setUp):
        print("测试 除法")
        print(f"{a}/{b}={Calculator().div(a, b)}")
