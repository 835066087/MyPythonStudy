#数组实现法
names = ['wang','li','sun']
scores = [100,104,80]

if names.__contains__('wang'):
    print(names.index('wang'))

print(names[0],'=',scores[0])

#Dict
d = {'wang':100,'li':104,'sun':80}
print(d['wang'])

#判断key是否在Dict内
print('Thomas' in d)
print(d.get('Thomas'))

#Set
s1 = set([1,2,3,4,5])
s2 = set([2,4,6,8,10])
print(s1 & s2)
print(s1 | s2)



d1 = {'xiaowang':(1,[2,3]),'xiaoli':2}

#print(d['xiaoli'])
