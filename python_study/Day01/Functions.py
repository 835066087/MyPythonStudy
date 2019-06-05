import math

print(abs(-10))
print(max(10,20,30))

n1 = 255
n2 = 1000
print(hex(n1))
print(hex(n2))


def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(100))


#如果你已经把my_abs()的函数定义保存为abstest.py文件了
#那么,可以在该文件的当前目录下启动Python解释器
#用from abstest import my_abs来导入my_abs()函数
#注意abstest是文件名（不含.py扩展名）


#空函数
#作为占位符或是没想好要做什么的功能
def nop():
    pass

#返回多个值
def move(x,y,step,angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx,ny

x,y = move(100,100,60,math.pi / 6)
print(x,y)


def quadratic(a,b,c):
    x1 = (-b + (math.sqrt(math.pow(b,2) - 4 * a * c))) / (2 * a)
    x2 = (-b - (math.sqrt(math.pow(b,2) - 4 * a * c))) / (2 * a)
    return x1,x2

x1,x2 = quadratic(2,3,1)
print(x1,x2)

x3,x4 = quadratic(1,3,-4)
print(x3,x4)

def power(x,n):
    return math.pow(x,n)

y1 = power(10,2)
print(y1)

#默认参数
def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

print(enroll('Sarah','F'))

#可变参数
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(calc([1,101]))

#可变参数写法:可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple
def calc1(*numbers):
    sum1 = 0
    for n in numbers:
        sum1 = sum1 + n * n
    return sum1

print(calc1(1,2,3,2,3,4))

nums = [1,2,3]
print(calc1(*nums))

#关键字参数:关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person(name,age,**kw):
    print('name:',name,'age',age,'other:',kw)

extra = {'city':'Beijing','job':'Engineer'}
p1 = person('Jack',24,**extra)
print(p1)

#命名关键字参数

