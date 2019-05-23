#定义两个list,如果查找对应的成绩，list越长，耗时越长
# names = ['michel' , 'bob' , 'tracy']
# soures = ['80' , '71' , '93']

# 如果用dict实现，只需要一个“名字”-“成绩”的对照表，直接根据名字查找成绩，无论这个表有多大，查找速度都不会变慢。

d = {'michel' : 80, 'bob':71 , 'tracy':93}
print(d['bob'])
print(d['tracy'])
#如果key不存在，dict就会报错：
# d['Thomas']
#要避免key不存在的错误，有两种办法，一是通过in判断key是否存在：
print('Thomas' in d)
#二是通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value：
print(d.get('thomas'))
print(d.get('thomas',-1))  #如果key不存在，就定义值为-1
#删除key
d.pop('bob')
print(d)
#要创建一个set，需要提供一个list作为输入集合：
s = set([1,2,3])
print(s)
#传入的参数[1, 2, 3]是一个list，而显示的{1, 2, 3}只是告诉你这个set内部有1，2，3这3个元素
#重复元素在set中自动被过滤：
s2 = set([1,2,3,4,3,3,3,3,4,4])
print(s2)
#通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果：
# s2.add(5)
# print(s2)
s2.remove(2)
print(s2)
#set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：
s10 = set([1,2,3,4])
s11 = set([2,3,4,5,6])
print(s10 & s11)
print(s10 | s11)