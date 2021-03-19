# 1.获取后缀
import os
file_ext = os.path.splitext('json.txt')
front, ext = file_ext
print(front, ext)

# 2.文件读操作
# 建立文件夹
def mkdir(path):
    isexists = os.path.exists(path)
    if not isexists:
        os.mkdir(path)

# 读取文件信息
def openfile(filename):
    f = open(filename)
    filelist = f.read()
    f.close()
    return filelist

print(openfile('json.txt'))

# 3.文件读操作
# 写入文件信息
# w写入，如果文件存在，清空内容再写入，不存在则创建
f = open(r'test.txt', 'w', encoding='utf-8')
print(f.write("w模式写入"))
f.close()
print(openfile("test.txt"))
# 读取出错

# a写入，文件存在，则在内容后面追加，不存在则创建
f = open(r'test.txt', 'a', encoding='utf-8')
print(f.write("a模式写入"))
f.close()
print(openfile("test.txt"))

# with关键字，系统会自动关闭文件和处理异常
with open("test.txt", "w") as f:
    f.write("test with")

print(openfile("test.txt"))

# 4.路径中的文件名
file_ext = os.path.split('trdt/test/json.txt')
front, ext = file_ext
print(front, ext)

# 5.批量修改文件后缀
# 使用os和argparase模块
# 命令行调用
# 在demo中测试，方便

# 6.xls 2 xlsx
import os
def xls_to_xlsx(work_dir):
    old_ext, new_ext = '.xls', '.xlsx'
    for filename in os.listdir(work_dir):
        split_file = os.path.splitext(filename)
        file_ext = split_file[1]
        if old_ext == file_ext:
            newfile = split_file[0] + new_ext
            os.rename(
                os.path.join(work_dir, filename),
                os.path.join(work_dir, newfile)
            )
    print("完成重命名")
    print(os.listdir(work_dir))

# 7.定制文件不同行(这个参考的貌似有毛病)
# 比较两个文件在那些行内容不同，返回这些行的编号，行号编号从1开始
# 统计文件个数
# 统计行数
def statLineCnt(statfile):
    print('文件名:'+statfile)
    cnt = 0
    with open(statfile, encoding='utf-8') as f:
        while f.readline():
            cnt += 1
        return cnt

# 统计文件不同之处
def diff(more, cnt, less):
    difflist = []
    with open(less, encoding='utf-8') as l:
        with open(more, encoding='utf-8') as m:
            lines = l.readline()
            print(lines)
            for i, line in enumerate(lines):
                if line.strip() != m.readline().strip():
                    difflist.append(i)
        if cnt - i > 1:
            difflist.extend(range(i+1, cnt))
        return [no+1 for no in difflist]

def file_diff_line_nos(filaA, fileB):
    try:
        cntA = statLineCnt(filaA)
        cntB = statLineCnt(fileB)
        if cntA > cntB:
            return diff(filaA, cntA, fileB)
        return diff(fileB, cntB, filaA)
    except Exception as e:
        print(e)

# 8.获取制定后缀名的文件
def find_file(work_dir, extension='jpg'):
    lst = []
    for filename in os.listdir(work_dir):
        print(filename)
        splits = os.path.splitext(filename)
        ext = splits[1]
        if ext == '.'+extension:
            lst.append(filename)
    return lst

r = find_file('.', 'txt')
print(r)

# 9.批量获取文件修改时间
from datetime import datetime

print(f"当前时间:{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

def get_modify_time(indir):
    for root, _, files in os.walk(indir): #遍历目录和子目录
        for file in files:
            absfile = os.path.join(root, file)
            modtime = datetime.fromtimestamp(os.path.getmtime(absfile))
            now = datetime.now()
            difftime = now-modtime
            if difftime.days < 20:
                print(f"""{absfile}
                    修改时间[{modtime.strftime('%Y-%m-%d %H:%M:%S')}]
                    距今[{difftime.days:3d}天{difftime.seconds//3600:2d}时{difftime.seconds%3600//60:2d}]""")

# 10.批量压缩文件（还不是很懂其中的操作）
import zipfile
import time

def batch_zip(start_dir):
    start_dir = start_dir
    file_news = start_dir + '.zip'
    print(file_news)

    z = zipfile.ZipFile(file_news, 'w', zipfile.ZIP_DEFLATED)
    for dir_path, dir_names, file_names in os.walk(start_dir):
        f_path = dir_path.replace(start_dir, '') #没有这句的话就从根目录开始复制
        f_path = f_path and f_path + os.sep #实现当前文件夹及包含的所有文件的压缩
        for filename in file_names:
            z.write(os.path.join(dir_path, filename), f_path+filename)
    z.close()
    return  file_news

# print(batch_zip('test'))

# 11.32位加密
import hashlib
# 对字符实现32位加密

def hash_cry32(s):
    m = hashlib.md5()
    m.update(str(s).encode('utf-8'))
    return m.hexdigest()

print(hash_cry32('hhh'))

# 12.年的日历图
import calendar
from datetime import date
mydate = date.today()
year_calender_str = calendar.calendar(mydate.year)
print(f"{mydate.year}年的日历图：{year_calender_str}\n")

# 13.判断闰年
is_leap = calendar.isleap(mydate.year)
print_leap_str = '%s年是闰年' if is_leap else "%s不是闰年\n"
print(print_leap_str % mydate.year)

# 日历图
month_calendar_str = calendar.month(mydate.year, mydate.month)
print(f"{mydate.year}年-{mydate.month}月的日历图：{month_calendar_str}\n")

# 14.月有多少天
weekday, days = calendar.monthrange(mydate.year, mydate.month)
print(f'{mydate.year}-{mydate.month}第一天是{weekday},共有{days}天')

# 15.月的第一天
month_first_day = date(mydate.year, mydate.month, 1)
print(month_first_day)

# 16.最后一天
month_last_day = date(mydate.year, mydate.month, days)
print(month_last_day)

# 17.获取当前时间
from time import localtime, strftime
print(mydate)

today_time = datetime.today()
print(today_time)

local_time = localtime()
print(strftime("%Y-%m-%d %H:%M:%S", local_time))

# 18.字符时间转时间
from time import strptime
struct_time = strptime('2021-03-12 10:10:21', "%Y-%m-%d %H:%M:%S")
print(struct_time)

# 19.时间(对象)转字符时间
print(localtime())
print(strftime("%m-%d-%Y %H:%M:%S", localtime()))

# 20.默认启动主线程
import threading
# 返回当前线程
t = threading.current_thread()
print(t)

print(t.getName())
print(t.ident)
print(t.is_alive())

# 21.创建线程
# my_thread = threading.Thread()
my_thread = threading.Thread(name='my_thread')
# 线程的使用
def print_i(i):
    print('打印i:%d'%i)
my_thread = threading.Thread(target=print_i, args=(1,))
# my_thread.start()

# 开辟3个线程
def print_time():
    for _ in range(5): #每个线程打印5次
        time.sleep(0.1) #模拟逻辑处理的时间
        print("当前线程%s,打印结束时间为：%s"%(threading.current_thread().getName(), datetime.today()))

# threads = [threading.Thread(name='t%d'%(i,), target=print_time) for i in range(3)]
#
# [t.start() for t in threads]

# 22.多线程抢夺同一个变量
a = 0
def add1():
    global a
    a += 1
    print('%s adds a to 1: %d'%(threading.current_thread().getName(), a))

# threads = [threading.Thread(name='t%d'%(i,), target=add1) for i in range(10)]
# [t.start() for t in threads]

# 23.多线程暴露的问题
def add2():
    global a
    tmp = a+1
    time.sleep(0.2)
    a = tmp
    print('%s adds a to 1: %d'%(threading.current_thread().getName(), a))

# threads = [threading.Thread(name='t%d'%(i,), target=add2) for i in range(10)]
# [t.start() for t in threads]

# 24.加锁
# 某段代码只能单线程执行，上锁，其他线程等待
locka = threading.Lock()
# 通过acquire获得锁，release释放锁
def add3():
    global a
    try:
        locka.acquire()
        tmp = a+1
        time.sleep(0.2)
        a = tmp
    finally:
        locka.release()
    print('%s adds a to 1: %d' % (threading.current_thread().getName(), a))

# threads = [threading.Thread(name='t%d'%(i,), target=add3) for i in range(10)]
# [t.start() for t in threads]

# 25.time模块
# struct_time:9个整数组成的元组
# 此时此刻时间浮点数
seconds = time.time()
print("time:%s"%seconds)

# 时间数组
local_time = time.localtime(seconds)
print(local_time)

# 时间字符串
str_time = time.asctime(local_time)
print(str_time)

# 格式化字符串
format_time = time.strftime('%Y-%m-%d %H:%M:%S', local_time)
print(format_time)

# 26.4G内存处理10G文件
# 假设行间数据相关性为0
# way1
def python_read(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        while True:
            line = f.readline()
            if not line:
                return
            yield line

# way2:way1中每次IO操作只读取一行，影响效率
import pandas as pd
def pandas_read(filename, sep=',', chunksize=5):
    reader = pd.read_csv(filename, sep, chunksize=chunksize)
    while True:
        try:
            yield reader.get_chunk()
        except StopIteration:
            print('Done')
            break

if __name__ == '__main__':
    # g = python_read('README.md')
    g = pandas_read('README.md', sep='::')
    for c in g:
        print(c)



# yield示例
'''
# encoding:UTF-8
def yield_test(n):
    for i in range(n):
        yield call(i)
        print("in:", i)
        # 做一些其它的事情
    print("do something.")
    print("end.")


def call(i):
    return i * 2


# 使用for循环
for i in yield_test(5):
    print('out:', i)
'''