# 1.寻找第n次出现位置
def search_n(s, c, n):
    size = 0
    for i, x in enumerate(s):
        if x == c:
            size += 1
        if size == n:
            return i
    return -1

# 2.斐波那契数列
def fibonacci(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a+b

print(list(fibonacci(10)))

# 3.找出所有重复元素
from collections import Counter

def find_all_dup(lst):
    c = Counter(lst)
    return list(filter(lambda k: c[k] > 1, c))

print(find_all_dup([1,1,2,2,3,4,55,5,5,8]))

# 4.联合统计次数
a = ['apple', 'orange', 'computer', 'orange']
b = ['computer', 'orange']

ca = Counter(a)
cb = Counter(b)
print(ca + cb)

# 进一步抽象
def sumc(*c):
    if(len(c) < 1):
        return
    mapc = map(Counter, c)
    # print(list(mapc))
    s = Counter([])
    for ic in mapc: #ic 是一个Counter对象
        print(ic)
        s += ic
    return s

print(sumc(a, b, ['abc'], ['face', 'computer']))

# 5.groupby单字段分组
a = [{'date': '2019-12-15', 'weather': 'cloud'},
     {'date': '2019-12-13', 'weather': 'sunny'},
     {'date': '2019-12-14', 'weather': 'cloud'}]

from itertools import groupby
# 在使用grouby前必须按使用的字段排序
a.sort(key=lambda x:x['weather'])
for k, items in groupby(a, key=lambda x:x['weather']):
    print(k)
    for i in items:
        print(i)

# 6.itemgetter和key函数
# key函数的写法除了lambda，还可以使用itemgetter
from operator import itemgetter

a.sort(key=itemgetter('weather'))
for k, items in groupby(a, key=itemgetter('weather')):
    pass
# 一样的步骤

# 7.itemgetter是一个类，返回一个可调用的对象，参数可有多个
a.sort(key=itemgetter('weather', 'date'))
# 其他同上

# 8.sum函数计算和聚合同时做
# 聚合类函数sum、min、max的第一个参数是iterable类型
# 一般的做法
a = [4, 2, 5, 1]
sum([i+1 for i in a])
# 这样是生成一个相同长度的列表再使用sum聚合，使用yeild生成器就可以节约内存
sum(i+1 for i in a)
# 此时的i+1 for i in a是(i+1 for i in a)的简写，返回的是一个生成器对象

# 9.list分组
from math import ceil


def divide_iter(lst, n):
    if n <= 0:
        yield lst
        return
    i, div = 0, ceil(len(lst)/n)
    while i < n:
        yield lst[i*div: (i+1)*div]
        i += 1

# print(divide_iter([1,2,3,4,5,6],2))
print(list(divide_iter([1,2,3,4,5,6],2)))

# 10.列表全展开
a = [1, 2, [3, 4, [5, 6], 7], 8, ['python', 6], 9]


def function(lst):
    for i in lst:
        if type(i) == list:
            # from?
            yield from function(i)
        else:
            yield i


print(list(function(a)))

# 11.测试函数运行时间的装饰器!!!
import time


def timing_func(fn):
    def wrapper():
        start = time.time()
        fn()
        end = time.time()
        return end-start
    return wrapper

@timing_func
def test_list_append():
    lst = []
    for i in range(100000):
        lst.append(i)

@timing_func
def test_list_compara():
    [i for i in range(100000)]


a = test_list_append()
c = test_list_compara()
print(a)
print(c)

# 12.统计异常出现的次数和时间
import math
# 关于修饰器@
# https://www.jianshu.com/p/ab702e4d4ba7

def excepter(f):
    i = 0
    t1 = time.time()


    def wrapper():
        try:
            f()
        except Exception as e:
            nonlocal i
            i += 1
            print(f'{e.args[0]} : {i}')
            t2 = time.time()
            if i == n:
                print(f'spending time:{round(t2-t1,2)}')
    return wrapper


n = 10


# 两种异常：零除和数组越界
@excepter
def divide_zero_except():
    time.sleep(0.1)
    j = 1/(40-20*2)


# for _ in range(n):
#     divide_zero_except()

@excepter
def out_range_except():
    a = [1, 3, 5]
    time.sleep(0.1)
    print(a[3])

for _ in range(n):
    out_range_except()
    print(_+1)

# 疑点：i为什么不会被重置

# 13.测试运行时长的装饰器
# the same as 11

# 14.装饰器通俗理解
def call_print(f):
    def g():
        print('you\'re calling %s function'%(f.__name__,))
    return g

@call_print
def myfun():
    pass


myfun()

# 等价于
def myfun2():
    pass

myfun2 = call_print(myfun2) # 重点！！！！！！！！！！
myfun2()

# 15.定制递减迭代器
class Descend():
    def __init__(self, N):
        self.N = N
        self.a = 0
    def __iter__(self):
        return self
    def __next__(self):
        while self.a<self.N:
            self.N -= 1
            return self.N
        raise StopIteration


descend_iter = Descend(10)
print(list(descend_iter))
# 核心：__next__的迭代逻辑，raise中断迭代

