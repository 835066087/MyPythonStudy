# -*- coding:utf-8 -*-
#这是单行注释
'''

多行注释

'''

#基本变量与转义字符
print('你好')
num1 = 100
num2 = 100
print(True or False)
print(10/3)
print(10//3)
print(len('选举一致'))
print('I\'m ok.')
num1 += num2
print(num1)

#格式化字符
'''
%d decimal
%f float
%s String
%% 转义字符用法
'''
#passwd = input('请输入密码:')
#print('您刚刚输入的密码是:%s' %passwd)
#print('您刚刚输入的密码是:' + passwd)
print('您的排名是:%s%%' %100)
name = '小明'
age = 18
print("我的名字是%s,我的年龄是%d"%(name,age))

#运算符
'''
1.python 不同数据类型都可以参与运算
2.**幂运算
3.Python如何实现自增
'''
print('str'*20)

for i in [1,3,5,7,9]:
    print(i + 1)

qq = 1234;
p = 1345;
location = '不知道'

print('姓名:%s'%name)
print('QQ:%d'%qq)
print('手机号：%d'%p)
print('地址：北京市%s'%location)

#数据类型转换
a = '5 + 8'
print(a)
b=eval(a)





