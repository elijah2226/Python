# 1.反转字符串
st = "python"
# way1
print(reversed(st))
print(''.join(reversed(st)))
# way2
st[::-1]
print(st)

# 2.字符串切片
# 只有i是3或5的倍数才能截取到java或者python
st = [str('java'[i%3*4:]+'python'[i%5*6:] or i) for i in range(1,15)]
print(st)

# 3.join串联字符串
print('.'.join(st))

# 4.字符串的字节长度
def str_byte_len(mystr):
    return len(mystr.encode('utf-8'))

print(str_byte_len('I love python'))
print(str_byte_len('字符'))


# 正则部分
import re

# 5.查找第一个匹配串
s = 'I love python very much'
pat = 'python'
r = re.search(pat,s)
print(r)
print(r.span())

# 6.查找所有1的索引
s = '山东潍坊青州第1中学高三1班'
pat = '1'
r = re.finditer(pat,s)
for i in r:
    print(i)

# 7.\d 匹配数字 [0-9]
s = '一共20行代码运行时间13.59s'
pat = r'\d+' # +表示匹配数字1次或多次
r = re.findall(pat,s)
print(r)

# 8.匹配浮点数和整数
# ?表示前一个字符匹配0/1次
pat = r'\d+\.?\d+' #该写法不能匹配到个位数的整数
r = re.findall(pat,s)
print(r)

pat = r'\d+\.?\d+|\d+' #A|B表示匹配A失败匹配B

# 9.^匹配字符串的开头
s = 'This module provides regular expression matching operations similar to those found in Perl'
pat = r'^[emrt]' #查找以字符e m r t开头的字符（整个字符串，而不是单词）
r = re.findall(pat,s)
print(r)
s = 'email for me is guozhennianhua@163.com'
pat = r'^[emrt].*' #以字符e m r t开始，后面任意多字符的字符串
r = re.findall(pat,s)
print(r)

# 10.re.l忽略大小写
s = 'That'
pat = r't'
r = re.findall(pat,s,re.I)
print(r)

# 11.理解compile的作用
# 如果要做很多次匹配，可以先编译字符串
pat = re.compile('\W+') #\W 匹配不是数字和字母的字符
has_special_chars = pat.search('ed#2@edc')
if has_special_chars:
    print(f'str contains special characters:{has_special_chars.group(0)}')

print(has_special_chars)

again_pattern = pat.findall('guozhannianhuaX@163.com')
print(again_pattern)
if '@' in again_pattern:
    print('yes')

# 12.使用()捕获单词，不想带空格
s = 'This module provides regular expression matching operations similar to those found in Perl'
pat = r'\s([a-zA-z]+)' #\s表示匹配空格,[]表示匹配的范围，+表示个数不限制
r = re.findall(pat, s)
print(r)
pat = r'\s?([a-zA-Z]+)'
r = re.findall(pat, s)
print(r)

# 13.split分割单词
# 使用以上方法分割单词不是简洁的，仅仅是为了演示。分割单词最简单还是使用split 函数。
pat = r'\s+'
r = re.split(pat, s)
print(r)
# split更简单
print(s.split(' '))
# 对于更复杂的情况就只能使用正则
s = 'This,,,   module ; \t   provides|| regular ; '
print(s)
words = re.split('[,\s;|]+',s)
print(words)
words = [i for i in words if len(i)>0]

# 14.match从字符串开始位置匹配
# 注意match和search的不同
mystr = 'This'
pat = re.compile('hi')
print(pat.match(mystr))
print(pat.match(mystr, 1))
# different
print(pat.search(mystr))

# 15.替代匹配的子串
# sub函数实现对匹配子串的替代
content = 'hello 12345, hello 456321'
pat = re.compile(r'\d+') #要被替换的部分
m = pat.sub('66', content)
print(m)

# 16.贪心捕获
# (.*)表示捕获任意多个字符
content = '<h>ddedadsad</h><div>graph</div>bb<div>math</div>cc'
pat = re.compile(r"<div>(.*)</div>") #贪婪模式
m = pat.findall(content)
print(m)

# 17.非贪婪捕获
pat = re.compile(r'<div>(.*?)</div>')
m = pat.findall(content)
print(m)

# 18.常用元字符
# . 匹配任意字符
# ^ 匹配字符串开始位置
# $ 匹配字符串中结束的位置
# * 前面的原子重复0次、1次、多次
# ? 前面的原子重复0次或者1次
# + 前面的原子重复1次或多次
# {n} 前面的原子出现了 n 次
# {n,} 前面的原子至少出现 n 次
# {n,m} 前面的原子出现次数介于 n-m 之间
# ( ) 分组,需要输出的部分

# 19.常用通用字符总结
# \s  匹配空白字符
# \w  匹配任意字母/数字/下划线
# \W  和小写 w 相反，匹配任意字母/数字/下划线以外的字符
# \d  匹配十进制数字
# \D  匹配除了十进制数以外的值
# [0-9]  匹配一个0-9之间的数字
# [a-z]  匹配小写英文字母
# [A-Z]  匹配大写英文字母

# 20.密码安全检查
# 要求：密码6-20位，只包含字母和数字
pat = re.compile(r'\w{6,20}')
# 错误，含有下划线
pat = re.compile(r'[\da-zA-Z]{6,20}')
# 选用最保险的fullmatch方法，查看整个字符串是否都匹配
print(pat.fullmatch('qaz12'))
print(pat.fullmatch('qaz_231'))
print(pat.fullmatch('n0passw0Rd'))

# 21.爬取百度首页标题
from urllib import request

# 爬虫爬取百度首页内容
data = request.urlopen("http://www.baidu.com/").read().decode()
# print(data)

# 分析网页，确定正则表达式
pat = r'<title>(.*?)</title>'

result = re.search(pat, data)
print(result)

# 22.批量转化为驼峰格式
# 用到的正则串讲解
# \s 指匹配： [ \t\n\r\f\v]
# A|B：表示匹配A串或B串
# re.sub(pattern, newchar, string):
# substitue代替，用newchar字符替代与pattern匹配的字符所有.

# title(): 转化为大写，例子：
# 'Hello world'.title() # 'Hello World'

print(re.sub(r"\s|_", "", "He llo_worl\td"))
s = re.sub(r'(\s|_|-)+', " ", "some_database_field_name").title().replace(" ", "")
print(s)
# 第一个大写需转小写
s = s[0].lower()+s[1:]
print(s)

# 封装
def camel(s):
    s = re.sub(r"(\s|_|-)+", " ", s).title().replace(" ", "")
    return s[0].lower()+s[1:]

# 批量转化
def batch_camel(slist):
    return [camel(s) for s in slist]

s = batch_camel(['student_id', 'student\tname', 'student-add'])
print(s)

# 23.str1是否为str2的permutation：含有相同字符，但是顺序不同
from collections import defaultdict

def is_permutation(str1, str2):
    if str1 is None or str2 is None:
        return False
    if len(str1) != len(str2):
        return False
    unq_s1 = defaultdict(int)
    unq_s2 = defaultdict(int)
    for c1 in str1:
        unq_s1[c1] += 1
    for c2 in str2:
        unq_s2[c2] += 1
    return unq_s1 == unq_s2


r = is_permutation('nice', 'cine')
print(r) # True

# 24.str1是否由str2旋转而来
# stringbook旋转得到bookstring
# 思路：str1是否是str2+str2的子串
def is_rotation(s1:str, s2:str) -> bool:
    if s1 is None or s2 is None:
        return False
    if len(s1) != len(s2):
        return False

    def is_substring(s1:str, s2:str) -> bool:
        return s1 in s2
    return is_substring(s1, s2+s2)

r = is_rotation('stringbook', 'bookstring')
print(r)

# 25.正浮点数
# ^[1-9]\d*\.\d*$ 连起来就求出所有大于 1.0 的正浮点数。
# ^表示字符串开始
# [1-9]表示数字1-9
# \d表示0-9的数字
# *表示出现多次
# \.表示小数点
# $表示字符串以前一位的字符结束

# 那 0.0 到 1.0 之间的正浮点数，^[0-9]\d*\.\d*$
recom = re.compile(r'^[0-9]\d*\.\d*$')
print(recom.match('000.2'))
# 不正确,应该是 ^0\.\d*[1-9]\d*$

# 最终应该是 ^[1-9]\d*\.\d*|0\.\d*[1-9]\d*$
