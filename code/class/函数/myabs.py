def my_abs(x):
    if not isinstance(x,(int, float)):
        raise TypeError('错误的数据类型')
    if x >=0:
        return x
    else:
        return -x
