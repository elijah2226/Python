# Python
## 序列（容器）
- 列表list，类似于c++的vector
- 元组tuple
- 字典dict，类似于map
- 集合set
## 关键字
- pass
- assert：判断表达式的真假，假则报错
## 函数
- range():Python内置函数
- zip():它可以将多个序列（列表、元组、字典、集合、字符串以及 range() 区间构成的列表）“压缩”成一个 zip 对象。所谓“压缩”，其实就是将这些序列中对应位置的元素重新组合，生成一个个新的元组。
## 自定义函数

def 函数名(参数列表):
    //实现特定功能的多行代码
    [return [返回值]]

函数说明文档
help(str_max)
## 函数闭包
相当于C++中的STL函数原型，返回函数指针

## lambda 表达式，又称匿名函数
常用来表示内部仅包含 1 行表达式的函数
name = lambda [list] : 表达式
###
def name(list):
    return 表达式
name(list)
###
- 对于单行函数，使用 lambda 表达式可以省去定义函数的过程，让代码更加简洁；
- 对于不需要多次复用的函数，使用 lambda 表达式可以在用完之后立即释放，提高程序执行的性能。

## eval()和exec()
eval() 和 exec() 函数的功能是相似的，都可以执行一个字符串形式的 Python 代码（代码以字符串的形式提供），相当于一个 Python 的解释器。
二者不同之处在于，eval() 执行完要返回结果，而 exec() 执行完不返回结果（文章后续会给出详细示例）
