'''
1. 接口测试场景比较难模拟，需要大量的工作才能完成。
2. 依赖第三方的接口，但是第三方的接口没有开发完成
测试环境不充分的情况下，怎么去做接口测试？使用Mock来模拟。
'''
from unittest import mock
import requests

class AliPay:
    def zhifu(self, data):
        # 接口功能尚未开发完成、
        # 接口地址、get\post、入参、返回值已经定义好，有对应的接口文档
        # 接口参数：'OrderId':'23498723497234', 'Amount': 128.5, 'Type': '支付宝'
        # 接口返回值：'code': 200, 'msg': '支付成功'  201：支付失败 202：支付超时
        r = requests.post('http://zhifubao.com/pay', data=data).json()
        return r

class TestMock:
    def test_alipay(self):
        # 对要模拟的类创建一个对象
        aliPay = AliPay()
        # 模拟zhifu的返回值为{‘code’：200，‘msg'：’支付成功‘
        aliPay.zhifu = mock.Mock(return_value={'code': 200, 'msg': '支付成功'})
        # 调用zhifu接口
        data = {'OrderId': '23498723497234', 'Amount': 128.5, 'Type': '支付宝'}
        r = aliPay.zhifu(data)
        print(r)

