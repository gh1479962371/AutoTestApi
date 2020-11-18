'''
fixture 可以带参数和返回值
'''

import pytest

# 测试前置：准备测试数据，在测试用例中使用测试数据。测试数据使用fixture的返回值来表示
@pytest.fixture()
def username_pwd():
    return {'username': 'root', 'pwd': 123456}  # 可以返回任意类型的数据

def test_login(username_pwd):
    print(f"测试数据为：{username_pwd['username']}")    # f:是格式化

# 相同的测试用例，只是每次输入的数据不同
@pytest.fixture(params=['root', 'admin', 'administrator', '12313'])  # 多组用户名
def data(request):    # request是固定写法，取到每一组数据
    return request.param    # request.param是固定写法，取到每一组数据

@pytest.fixture(params=[
    {'casedata': 'root', 'expect': '成功'},
    {'casedata': 'admin', 'expect': '失败'}])   # 多组用户名
def data1(request):
    return request.param

def test_login2(data):
    print(f'使用用户名{data}测试登录功能')

def test_login3(data1):
    print(f"使用用户名{data1['casedata']}测试登录功能,预期结果为{data1['expect']}")
