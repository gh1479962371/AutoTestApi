'''
python测试命名规则：
1、测试文件以test_开头或者结尾
2、测试类以Test开头
3、测试方法以test_开头
'''
import requests

def register(data):
    url = "http://jy001:8081/futureloan/mvc/api/member/register"
    r = requests.post(url, data=data)
    return r

# 手机号格式不正确
def test_register_001():
    # 测试数据
    data = {'mobilephone': 180125256712, 'pwd': 123456, 'regname': 'hello'}
    # 预期结果
    expect = {'status': 0, 'code': '20109', 'data': None, 'msg': '手机号码格式不正确'}
    # print(json.dumps(data))  # 字典转json
    # 测试步骤
    real = register(data)
    # 检查结果
    assert real.json()['msg'] == expect['msg']
    assert real.json()['code'] == expect['code']

def test_register_002():
    data = {'mobilephone': '1801234567a', 'pwd': 123456, 'regname': 'hello'}
    expect = {'status': 0, 'code': '20109', 'data': None, 'msg': '手机号码格式不正确'}
    real = register(data)
    assert real.json()['msg'] == expect['msg']
    assert real.json()['code'] == expect['code']

def test_register_003():
    data = {'mobilephone': 18013542112, 'pwd': None, 'regname': 'hello'}
    expect = {'status': 0, 'code': '20103', 'data': None, 'msg': '参数错误：参数不能为空'}
    real = register(data)
    assert real.json()['msg'] == expect['msg']
    assert real.json()['code'] == expect['code']
