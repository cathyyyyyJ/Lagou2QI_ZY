import pytest
import yaml


def pytest_addoption(parser):
    mygroup = parser.getgroup("hogwarts")
    mygroup.addoption("--env",
                      default='test',
                      dest='env',
                      help='set your run env')


@pytest.fixture(scope='session')
def cmdoption(request):
    myenv=request.config.getoption("--env",default='test')
    if myenv =='test':
        print("获取测试数据")
        with open("E:/project/pycharm/TASK/pythoncode4/env/test.yml") as f:
            datas = yaml.safe_load(f)
    elif myenv == 'dev':
        print("获取dev数据")
        with open("E:/project/pycharm/TASK/pythoncode4/env/dev.yml")  as f:
            datas = yaml.safe_load(f)
    elif myenv== 'st':
        print("获取st数据")
        with open("E:/project/pycharm/TASK/pythoncode4/env/st.yml") as f:
            datas = yaml.safe_load(f)

    return datas