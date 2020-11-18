'''
测试登录功能
'''
import pytest

from ZongHe.baw import DbOp, Member
from ZongHe.caw import DataRead


@pytest.fixture(params=DataRead.readyaml('ZongHe/data_case/login_data.yaml'))
def login_data(request):
    return request.param

@pytest.fixture(params=DataRead.readyaml('ZongHe/data_case/login_setup.yaml'))
def setup_data(request):
    return request.param

# 测试前置和后置
@pytest.fixture()
def register(setup_data, db, url, baserequests):
    # 注册用户
    # 初始化环境，确保环境中没有影响本次执行的数据
    phone = setup_data['casedata']['mobilephone']
    DbOp.deleteUser(db, phone)
    Member.register(url, baserequests, setup_data['casedata'])
    yield
    # 删除注册的用户
    DbOp.deleteUser(db, phone)

def test_login(register, login_data, url, db, baserequests):
    # 登录
    r = Member.login(url, baserequests, login_data['casedata'])
    # # 检查登录的结果：检查响应结果
    assert str(r.json()['msg']) == str(login_data['expect']['msg'])
    assert str(r.json()['status']) == str(login_data['expect']['status'])
    assert str(r.json()['code']) == str(login_data['expect']['code'])
