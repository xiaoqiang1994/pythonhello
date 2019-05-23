#根据年龄打印不同的内容
age = 23
if age >= 23:
    print("you age is ", age )
    print('abult')

#根据Python的缩进规则，如果if语句判断是True，就把缩进的两行print语句执行了，否则，什么也不做。
# 也可以给if添加一个else语句，意思是，如果if判断是False，不要执行if的内容，去把else执行了
age = 13
if age >=18:
    print('your age is', age)
    print("成年人")
else:   #注意不要少了:号
    print('your age is', age)
    print("未成年人")
#用elif做更细致的判断
age = 3
if age >=18:
    print('your age is ', age)
    print ('成年人')
elif age >= 6:
    print("your age is", age )
    print("青少年")
else :
    print("your age is", age)
    print("小孩子")
# input使用
birth = input('InputBirth')
InputBirth = int(birth)   #因为input()返回的是str类型，str不能直接和int类型比较，必须把str转换成证书.用int（）来转换
if InputBirth < 2000:
    print("00前")
else:
    print("00后")
