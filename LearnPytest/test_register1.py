import requests
import pytest
import json

def register(data):
    url = "http://jy001:8081/futureloan/mvc/api/member/register"
    r = requests.post(url, data=data)
    return r

@pytest.fixture(params=[
    {'casedata': {'mobilephone': 1519591727, 'pwd': 123456, 'regname': 'hello'},
     'expect': {'status': 0, 'code': '20109', 'data': None, 'msg': '手机号码格式不正确'}},
    {'casedata': {'mobilephone': '151959172742', 'pwd': 123456, 'regname': 'hello'},
     'expect': {'status': 0, 'code': '20109', 'data': None, 'msg': '手机号码格式不正确'}},
    {'casedata': {'mobilephone': '18012525671a', 'pwd': 123456, 'regname': 'hello'},
     'expect': {'status': 0, 'code': '20109', 'data': None, 'msg': '手机号码格式不正确'}},
    {'casedata': {'mobilephone': 15195917275, 'pwd': 12345, 'regname': 'hello'},
     'expect': {'status': 0, 'code': '20108', 'data': None, 'msg': '密码长度必须为6~18'}},
    {'casedata': {'mobilephone': 15195917275, 'pwd': 1234567891234567891, 'regname': 'hello'},
     'expect': {'status': 0, 'code': '20108', 'data': None, 'msg': '密码长度必须为6~18'}}])
def register_data(request):
    return request.param

def test_register(register_data):
    real = register(register_data['casedata'])
    print(real.text)
    print(real.json())
    assert real.json()['msg'] == register_data['expect']['msg']
    assert real.json()['code'] == register_data['expect']['code']

