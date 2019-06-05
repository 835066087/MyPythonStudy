#简单的if条件
age = 20
if age >= 18:
    print('your age is',age)
    #Java写法是'your age is' + age，python打,
    print('adult')

age1 = 3
if age1 >= 18:
    print('adult')
elif age1 >= 6:
    print('teenager')
else:
    print('kid')


birth = input('birth')
#input输入的一定是str，需要强转
birthNum = int(birth)

if birthNum < 2000:
    print('00前')
else:
    print('00后')

t = input('tall:')
tall = float(t)
w = input('weigth:')
weight = float(w)

bmi = weight / (tall ** 2)
print('你的bmi指数为:',bmi)
if bmi > 32:
    print('严重肥胖')
elif bmi > 28:
    print('肥胖')
elif bmi > 25:
    print('过重')
elif bmi > 18.5:
    print('正常')
else:
    print('过轻')

