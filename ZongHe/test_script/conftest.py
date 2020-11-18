'''
脚本层的公共方法
'''
import pytest

from ZongHe.caw import DataRead   # 导入模块
from ZongHe.caw.BaseRequests import BaseRequests  # 从模块导入类

# 从环境文件中读取url
@pytest.fixture(scope='session')
def url():
    return DataRead.readini("ZongHe/data_env/env.ini", "url")

# 从环境文件中读取db
@pytest.fixture(scope='session')
def db():
    # 从ini中读取出来的是字符串，将字符串转成字典，使用eval函数
    return eval(DataRead.readini("ZongHe/data_env/env.ini", "db"))

# 创建BaseRequests的一个实例
@pytest.fixture(scope='session')
def baserequests():
    return BaseRequests()