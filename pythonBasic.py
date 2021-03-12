# python基础(内置函数)

# 1.绝对值
print(abs(-6))

# 2.检查所有元素的bool值
print(all([1, 0, 2, 4]))

# 3.检查任一元素有真值
print(any([0, 1, 0]))


# 4.It returns a string containing a printable representation of an object.
class Student():
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return 'id = ' + self.id + ', name = ' + self.name

    def __call__(self):
        print('Im called')
        # f用于格式控制?,中括号类似于数据绑定?
        print(f'my name is {self.name}')

    @classmethod
    def f(cls):
        # why after a None?
        print('Im classmethod')

xiaoming = Student(id='001', name='xiaoming')
print(xiaoming)
print(ascii(xiaoming))

# 5.10to2
print(bin(10))

# 6.10to8
print(oct(9))

# 7.10to16
print(hex(15))

# 8.判断单一对象bool值
print(bool([0, 1, 1]))

# 9.string to char
s = "apple"
print(bytes(s, encoding='utf-8'))

# 10.to string
print(str(100))

# 11.check callable
print(callable(int))
print(callable(xiaoming))

t = Student('002', 'xiaohong')
callable(t)
t()

# 12.10 to ascii
print(chr(66))

# 13.ascii to 10
print(ord('A'))

# 14.类方法中关键词 classmethod 修饰的方法不需要实例化(静态方法?),所以不需要self参数,但是需要代表自身类的cls参数,用来调用类的属性,方法,实例化对象
print(Student.f())

# 15.string to exe code
s = "print('Hello World')"
r = compile(s, "<string>", "exec")
exec(r)

# 16.复数
print(complex(4,5))

# 17.删除和检查对象属性
delattr(xiaoming, 'id')
print(hasattr(xiaoming, 'id'))

# 18.dirt字典
print(dict())
print(dict(a='a', b='b'))
print(dict(zip(['a','b'], [1,2])))
print(dict([('a',1), ('b',2)]))

# 19.查看对象
print(dir(xiaoming))

# 20.商与余
print(divmod(11,2))

# 21.枚举对象 函数返回一个带index(第二个参数是第一个index)的枚举对象
s = ['a', 'b', 'c']
for i, v in enumerate(s, 1):
    print(i, v)

# 22.string to count
s = '1+10*5'
print(eval(s))

# 23.check size
import sys
a = {'a':1, 'b':2}
print(sys.getsizeof(a))

# 24.filter
fil = filter(lambda x:x>10, [1, 15, 19, 8, 6])
print(list(fil))

# 25.to double
print(float(4))

# 26.format格式化输出
print("i am {0}, age{1}".format("tom",18))
print("i am {0}, age{1:.2f}".format("tom",18))

# 27.frozenset
print(frozenset([1,3,6]))

# 28.获取对象属性
print(getattr(xiaoming, 'name'))

# 29.检查对象属性同17

# 30.返回对象哈希值,自定义的实例都有哈希值,list,dict,set等可变对象不可哈希
print(hash(xiaoming))

# 31.返回对象的帮助文档
help(xiaoming)

# 32.对象内存地址
print(id(xiaoming))

# 33.获取输入
# input()

# 34.to int,第二个参数是进制 base of nub
print(int('12', 16))

# 35.判断对象是否是某类的实例
print(isinstance(xiaoming, Student))
print(isinstance(12, int))

# 36.父子类检测
class undergradute(Student):
    pass

print(issubclass(undergradute, Student))
print(issubclass(undergradute, object))
# 元素元组中的元素
print(issubclass(int, (int,float)))

# 37.迭代器
lst = [1,3,5]
for i in iter(lst):
    print(i)

class TestIter(object):
    def __init__(self):
        self.l=[1,2,3,4,5,6]
        self.i=iter(self.l)
    def __call__(self):
        item=next(self.i)
        print("调用call,迭代器向下")
        return item
    def __iter__(self):
#         支持迭代器协议
        print("调用iter,返回迭代器")
        return iter(self.l)

t = TestIter()
t()

for e in TestIter():
    print(e)

# 38.object所有对象的父
o = object()
print(type(o))

# 39.文件
fo = open('text.txt')
print(fo.read())

# 40.次幂
# pow(x, y) is equal to xy
# pow(x, y, z) is equal to xy % z
print(pow(2,5))

# 41.打印输出

# 42.属性的封装
class C:
    def __init__(self):
        self.x=None
    def getx(self):
        return self.x
    def setx(self, value):
        self.x=value
    def delx(self):
        del self.x
#   封装属性
    x = property(getx, setx, delx, "x property")

class CP:
    def __init__(self):
        self.x=None
    @property
    def x(self):
        return self.x
    @x.setter
    def x(self, value):
        self.x=value
    @x.deleter
    def x(self):
        del self.x

# 43.创建range序列(不可变)
print(list(range(0,19,2)))

# 44.逆转序列
rev = reversed([1,2,3,4,5,6])
for i in rev:
    print(i)

# 45.四舍五入
print(round(10.123456,4))

# 46.to set
a=[1,2,1,2,3,4]
print(set(a))

# 47.切片
a=[1,2,3,4,5,6,7,8]
myslice=slice(0,7,2)
print(a[myslice])

# 48.排序函数 成员函数sort()直接修改序列而不返回任何值，sorted()返回已排序的序列
a=[1,7,3,4,6,7]
a=sorted(a, reverse=True)
print(a)
a=[{'name':'xiaoming','age':19},{'name':'xiaohong','age':33},{'name0':'xiaohei','age':22}]
a.sort(key=lambda x:x['age'],reverse=True)
print(a)

# 49.求和函数
a=[1,2,3,4,5,6,7,8]
print(sum(a,100))

# 50.to tuple
t=tuple(a)
print(t)

# 51.查看类型
print(type(xiaoming))

# 52.聚合迭代器
x=[1,2,3]
y=[4,5,6]
print(list(zip(x,y)))
print([str(a)+str(b) for a,b in zip(x,y)])

# 53.nonlocal,用于内嵌函数中，表明一个变量为非局部变量
def outer():
    x='local'
    def inner():
        nonlocal x
        x='nonlocal'
        print(x)
    inner()
    print(x)

outer()

# 54.global,什么全局变量
i=0
def h():
    global i
    i+=1

h()
print(i)

# 55.链式比较
print(0<i<1)
print(0<i<=1)

# 56.不使用else if实现计算器
from operator import *
def calculator(a,b,k):
    return {
        '+':add,
        '-':sub,
        '*':mul,
        '/':truediv,
        '**':pow
    }[k](a,b)
# return后面是一个字典，字符串对应函数指针，字典取值得到函数指针，再调用函数
print(calculator(2,10,'+'))

# 57.链式操作
def addorsub(a,b,k):
    return  (add if k=='+' else sub)(a,b)

print(addorsub(10,3,'-'))

# 58.swap
def swap(a,b):
    return b,a

print(swap(10,1))

# 59.去最求平均
def score(lst):
    lst.sort()
    lst2=lst[1:(len(lst)-1)]
    return round(sum(lst2)/len(lst2),2)

print(score([1,2,3,4,5,6,5.6]))

# 60.打印乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print('%d*%d=%d'%(j,i,j*i),end="\t")
    print()

# 61.全展开（递归）
from _collections_abc import *
# 容器的抽象基类
def flatten(lst, out_lst=None):
    if out_lst is None:
        out_lst=[]
    for i in lst:
        if isinstance(i, Iterable):# 引入中的函数，判断容器是否可迭代（展开）
            flatten(i, out_lst)
        else:
            out_lst.append(i)
    return out_lst

print(flatten([[12,3,4],[5,0]]))

# 62.列表等分
from math import ceil
# ceil函数返回一个大于或等于x的的最小整数。
def divide(lst, size):
    if size<=0:
        return [lst]
    return [lst[i*size:(i+1)*size] for i in range(0, ceil(len(lst)/size))]

r = divide([1,23,4,45,5,6,76,8,0], 2)
print(r)

# 63.列表压缩
def filter_false(lst):
    return list(filter(bool,lst))

r = filter_false([None, 0, False, '', [], 'ok', [1,2]])
print(r)

# 64.求最长数组
def max_length(*lst):# *号表示列表的数组
    return  max(*lst, key=lambda v:len(v))

r = max_length([12,2,3,4],[1,2,3,4,5],[2,3])
print(r)

# 65.求众数
def top1(lst):
    return max(lst, default='空列表', key=lambda v:lst.count(v))

lst = [1,1,1,1,2,2,3,4,5,6]
r = top1(lst)
print(r)

# 66.多表之最
def max_list(*lst):
    return  max(max(*lst, key=lambda v:max(v)))
# 最里面的max用于比较各个序列的标准，第二个max返回含最大数的序列，第三个max取出最大的数


r = max_list([1,2,3,2,3,5],[4,5,6,9],[6,7,8])
print(r)

# 67.列表查重
def has_duplicates(lst):
    return len(lst) == len(set(lst))

x=[1,1,1,2,3,4,5,6,3,5,5,8]
print(has_duplicates(x))

# 68.列表反转
def reverse(lst):
    return lst[::-1]

r = reverse([1,2,3,4,4,5,5,9])
print(r)

# 69.浮点数等差数列
def rang(start, end, n):
    start, end, n = float('%.2f'%start), float('%.2f'%end), int('%d'%n)
    step = (end-start)/n
    lst = [start]
    while n>0:
        start,n = start+step,n-1
        lst.append(round(start,2))
    return lst

print(rang(1,8,10))
# 70.按条件分组
def bif_by(lst, f):
    return [[x for x in lst if f(x)],[x for x in lst if not f(x)]]

records=[1,24,2,4,65,7,4]
print(bif_by(records, lambda x:x>20))

# 71.map实现向量运算
lst1=[1,2,3,4,5,6]
lst2=[7,2,3,5,6,7]
print(list(map(lambda x,y:x*y, lst1, lst2)))

# 72.值最大的字典
def max_pairs(dic):
    if len(dic)==0:
        return  dic
    max_val = max(map(lambda v:v[1], dic.items()))
    return [item for item in dic.items() if item[1] == max_val]

r=max_pairs({'a':-10,'b':5,'c':3,'d':5})
print(r)

# 73.合并两个字典
def merge_dict(dic1, dic2):
    print(dic1)
    print(*dic1)
    # print(**dic1)报错
    return {**dic1, **dic2}
# https://blog.csdn.net/qq_35664993/article/details/53182959
# https://blog.csdn.net/KINGSUO2016/article/details/78614686
# * 用来传递任意个无名字参数，这些参数会一个元组的形式访问。
# **用来处理传递任意个有名字的参数，这些参数用字典来访问。
print(merge_dict({'a':1, 'b':2}, {'c':3}))

# 74.topn字典
from heapq import nlargest

def topn_dict(d,n):
    return nlargest(n, d, key=lambda k:d[k])

t = {'a':10,'b':8,'c':9,'d':10}
for i in t:
    print(t[i])

print(topn_dict({'a':10,'b':8,'c':9,'d':10},3))

# 75.异位词
from collections import Counter
# A Counter is a container that keeps track of how many times equivalent values are added.
def anagram(str1, str2):
    return  Counter(str1)==Counter(str2)

print(anagram('eleven+two','twelve+one'))

# 76.逻辑合并字典
dic1 = {'x':1,'y':2}
dic2 = {'y':3,'z':4}
merged1 ={**dic1,**dic2}
print(merged1)
# 重新生成一个字典
from collections import ChainMap
merged2 = ChainMap(dic1,dic2)
print(merged2)

# 77.命名元组提高可读性
from collections import namedtuple

Point = namedtuple('Point', ['x','y','z'])
# 定义名字为Point的元组，字段属性有xyz
lst = [Point(1.5, 2, 3), Point(-0.3, -1, 2.1), Point(1.3, 2.8, -2.5)]
print(lst[0].y-lst[1].y)

# 78.样本抽样
from random import randint,sample
# randint(a, b)
# Return a random integer N such that a <= N <= b
lst = [randint(0,50) for _ in range(100)]
print(lst[:10])
lst_sample = sample(lst, 10)
print(lst_sample)

# 79.重洗数据集，就地洗牌
from random import shuffle
shuffle(lst)
print(lst[:10])

# 80.均匀分布的坐标点
from random import uniform
print([(uniform(0,10),uniform(0,10))for _ in range(10)])

# 81.高斯分布
from random import gauss
x = range(10)
y = [2*xi+1+gauss(0,1) for xi in x]
print(y)
points = list(zip(x,y))
print(points)

# 82.chain串联多个容器对象
from itertools import chain
a=[1,3,5,0]
b=(2,4,6)
print(list(chain(a,b)))

# 83.操作函数对象
def f():
    print("Im f")

def g():
    print("Im g")

[f,g][1]()
# 对于函数数组，调用了第二个函数

# 84.生成逆序
print(list(range(10,0,-1)))

# 85.函数的五类参数应用
# 位置参数、关键字参数、默认参数、可变位置/关键字参数
def f(a, *b, c=10, **d):
    print(f'a:{a},b:{b},c:{c},d:{d}')

f(1, 2, 5, width=10, height=20)

f(a=1, c=12)

# 86.slice对象
cake1 = list(range(5, 0, -1))
b = cake1[1:10:2]
print(b)

# 封装
perfect_cake_slice_way = slice(1,10,2)
print(cake1[perfect_cake_slice_way])

# 87.lambda函数动画演示
# 不表

# 88.粘性之禅???
def product(*args, repeat=1):
    pools = [tuple(pool) for pool in args] *repeat
    print(pools)
    result = []
    for pool in pools:
        print('pool:',pool)
        result = [x+[y] for x in result for y in pool]
        print('result:',result)
    for prod in result:
        yield tuple(prod)

rtn = product('xyz','12',repeat=3)
print(list(rtn))

# 89.元类（类的类）
class Student(object):
    pass

xiaoming = Student()
print(xiaoming.__class__)
print(Student.__class__)
# Student类也是对象
Student = type('Student',(),{})
print(Student)

# 90.对象序列化
class Student():
    def __init__(self,**args):
        self.ids=args['ids']
        self.name=args['name']
        self.address=args['address']

xiaoming = Student(ids=1, name='xiaoming', address='北京')
xiaohong = Student(ids=2, name='xiaohong', address='南京')

# 导入json模块，调用dump方法
import json

with open('json.txt', 'w') as f:
    json.dump([xiaoming, xiaohong], f, default=lambda obj: obj.__dict__, ensure_ascii=False, indent=2, sort_keys=True)

