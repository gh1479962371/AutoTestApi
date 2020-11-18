# 注册
import unittest

import requests
url1 = "http://jy001:8081/futureloan/mvc/api/member/register"
url2 = "http://jy001:8081/futureloan/mvc/api/member/login"
s = '{"status":0,"code":"20109","data":null,"msg":"手机号码格式不正确"}'
s1 = '{"status":0,"code":"20103","data":null,"msg":"手机号不能为空"}'
s2 = '{"status":0,"code":"20110","data":null,"msg":"手机号码已被注册"}'
s3 = '{"status":"0",code":"20108","data":null,"msg":"密码长度必须为6~18"}'
s4 = '{"status":0,"code":"20103","data":null",msg":"参数错误：参数不能为空"}'
s5 = '{"status":0,"code":"20102","data":null,"msg":"服务器异常"}'
s6 = '{"status":"1","code":"10001","msg":"注册成功"}'
s7 = '{"status":0,"code":"20111","data":null,"msg":"用户名或密码错误"}'
s8 = '{"status":"0","code":"20103","msg":"参数错误：参数不能为空"}'
s9 = '{"status":0,"code":"20103","data":null,"msg":"手机号不能为空"}'
s10 = '{"status":1,"code":"10001","data":null,"msg":"登录成功"}'

# ZhuCe = {"pwd": "123456abc", "regname": "aaa"}
# a = requests.post(url1, data=ZhuCe)
# print(a.text)
# assert a.text == s1
#
# ZhuCe = {"mobilephone": "137123456789", "pwd": "123456abc", "regname": "aaa"}
# a = requests.post(url1, data=ZhuCe)
# print(a.text)
# assert a.text == s
#
# ZhuCe = '{"mobilephone":"137","pwd":"123456abc","regname":"aaa"}'
# a = requests.post(url1, data=ZhuCe)
# print(a.text)
# assert a.text == s1
#
# ZhuCe = '{"mobilephone":"1371234111a","pwd":"123456abc","regname":"aaa"}'
# a = requests.post(url1, data=ZhuCe)
# print(a.text)
# assert a.text == s1
# #
# # ZhuCe = '{"mobilephone":"1371234444#","pwd":"123456abc","regname":"aaa"}'
# # a = requests.post(url1, data=ZhuCe)
# # print(a.text)
# # assert a.text == s
# #
# # ZhuCe = '{"mobilephone":"13745241111","pwd":"123456abc","regname":"aaa"}'
# # a = requests.post(url1, data=ZhuCe)
# # print(a.text)
# # assert a.text == s2
#
# # ZhuCe = '{"mobilephone":"13711111111","pwd":"123456abc","regname":"aaa"}'
# # a = requests.post(url1, data=ZhuCe)
# # print(a.text)
# # assert a.text == s
# #
# # ZhuCe = '{"mobilephone":"13745241112","pwd":"12345678901234567890","regname":"aaa"}'
# # a = requests.post(url1, data=ZhuCe)
# # print(a.text)
# # assert a.text == s3
# #
# # ZhuCe = '{"mobilephone":"13745241112","pwd":"12345","regname":"aaa"}'
# # a = requests.post(url1, data=ZhuCe)
# # print(a.text)
# # assert a.text == s3
# #
# # ZhuCe = '{"mobilephone":"13745241112","pwd":null,"regname":"aaa"}'
# # a = requests.post(url1, data=ZhuCe)
# # print(a.text)
# # assert a.text == s4
# #
# # ZhuCe = '{"mobilephone":"13745241112","pwd":"123456abc","regname":"1111111111111111111111111111111111"}'
# # a = requests.post(url1, data=ZhuCe)
# # print(a.text)
# # assert a.text == s5
# #
ZhuCe = '{"mobilephone":"15289274915","pwd":"123456","regname":"null"}'
a = requests.post(url1, data=ZhuCe)
print(a.text)
# assert a.text == s6
#
# ZhuCe = '{"mobilephone":"13745241112","pwd":"123456789012345678","regname":"aaa"}'
# a = requests.post(url1, data=ZhuCe)
# print(a.text)
# assert a.text == s6
#
# ZhuCe = '{"mobilephone":"13745241112","pwd":"1234567890123","regname":"null"}'
# a = requests.post(url1, data=ZhuCe)
# print(a.text)
# assert a.text == s6
#
# # 登录
#
# DengLu = {"mobilephone": "12345678912", "pwd": "12345"}
# b = requests.post(url2, data=DengLu)
# print(b.text)
# assert b.text == s7
#
# DengLu = {"mobilephone": "12345678913", "pwd": "123456789qwertyuiop"}
# b = requests.post(url2, data=DengLu)
# print(b.text)
# assert b.text == s7
#
# DengLu = {"mobilephone": "12345678913", "pwd": ""}
# b = requests.post(url2, data=DengLu)
# print(b.text)
# assert b.text == s8
#
# DengLu = {"mobilephone": "123456789", "pwd": "qwerty"}
# b = requests.post(url2, data=DengLu)
# print(b.text)
# assert b.text == s7
#
# DengLu = {"mobilephone": "123456789102", "pwd": "qwerty"}
# b = requests.post(url2, data=DengLu)
# print(b.text)
# assert b.text == s7
#
# DengLu = {"mobilephone": "", "pwd": "qwertyuio"}
# b = requests.post(url2, data=DengLu)
# print(b.text)
# assert b.text == s9
#
# DengLu = {"mobilephone": "", "pwd": ""}
# b = requests.post(url2, data=DengLu)
# print(b.text)
# assert b.text == s9
#
# DengLu = {"mobilephone": "1234567890a", "pwd": "qwerty"}
# b = requests.post(url2, data=DengLu)
# print(b.text)
# assert b.text == s7
#
# DengLu = {"mobilephone": "123456@7891", "pwd": "qwerty"}
# b = requests.post(url2, data=DengLu)
# print(b.text)
# assert b.text == s7
#
# DengLu = {"mobilephone": "11111111111", "pwd": "qwerty7354"}
# b = requests.post(url2, data=DengLu)
# print(b.text)
# assert b.text == s7
#
# DengLu = {"mobilephone": "13745241111", "pwd": "123456abc"}
# b = requests.post(url2, data=DengLu)
# print(b.text)
# assert b.text == s10
# #
