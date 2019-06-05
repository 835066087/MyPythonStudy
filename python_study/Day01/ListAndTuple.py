classmates = ['Michael','Bob','Tracy']
print(classmates[1])

#数组的基本操作：增删改查
#增
classmates.append('XiaoWangba')
classmates.append('LaoWangba')
classmates.append(1);
print(classmates)
#插
classmates.insert(1,'Old Bob')

#删
classmates.remove('Bob')
print(classmates)

classmates.pop()
print(classmates)

classmates.pop(1)
print(classmates)

#改
classmates[1] = 'Wang';
print(classmates)

#二维数组与多维数组（这里只写到了三维数组操作）
num = [1,2,3,4,5,[5,6,7,8,9,10,[10,11,12]]]
print(num[5][6][0])


#元组 tuple,类似于Java的String
xiaoLaoDi = ('Michael','Bob','Tracy')
print(xiaoLaoDi)

t=(1,)

t1 = ('a','b',['A','B'])
t1[2][0] = 1;
print(t1)



