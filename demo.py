import argparse
import os

'''
# 基础
parser = argparse.ArgumentParser()
parser.add_argument("echo", help="echo the string you use here")
args = parser.parse_args()
print(args.echo)

# 关于位置参数（必要的）
# 创建一个命令行对象
parser = argparse.ArgumentParser()
# 调用添加参数函数
parser.add_argument("square", help="display a square of a given number", type=int)
# 获取参数序列
args = parser.parse_args()
print(args.square**2)

# 关于可选参数
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbosity", help="increasse output verbosity", action="store_true")
args = parser.parse_args()
if args.verbosity:
    print("verbosity turned on")
'''
def get_parser():
    parser = argparse.ArgumentParser(description="在工作目录中文件后缀名修改")
    parser.add_argument("work_dir", metavar="WORK_DIR", type=str, nargs=1, help='修改后缀名的文件目录')
    parser.add_argument('old_ext', metavar="OLD_EXT", type=str, nargs=1, help="原来的后缀")
    parser.add_argument('new_ext', metavar="NEW_EXT", type=str, nargs=1, help="新的后缀")
    return parser


def batch_rename(work_dir, old_ext, new_ext):
    for filename in os.listdir(work_dir):
        split_file = os.path.splitext(filename)
        file_ext = split_file[1]
        if old_ext == file_ext:
            newfile = split_file[0] + new_ext
            # 重命名操作
            os.rename(
                os.path.join(work_dir, filename),
                os.path.join(work_dir, newfile)
            )
    print("完成重命名")
    print(os.listdir(work_dir))

def main():
    # 命令行参数
    parser = get_parser()
    print(parser)
    args = vars(parser.parse_args())
    print(args)
    # 从命令行参数解析出参数
    work_dir = args['work_dir'][0]
    old_ext = args['old_ext'][0]
    if old_ext[0] != '.':
        old_ext = '.'+old_ext
    new_ext = args['new_ext'][0]
    if new_ext[0] != '.':
        new_ext = '.'+new_ext

    batch_rename(work_dir, old_ext, new_ext)

main()