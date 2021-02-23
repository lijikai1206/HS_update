import os
import time
import shutil


def is_dir_exist(path):
    if not os.path.exists(path):
        os.mkdir(path)
    return True


def get_curtime(format_str = "%Y-%m-%d %H:%M:%S"):
    ct = time.strftime(format_str, time.localtime())
    return ct


def delete_dir(path, re_mkdir=False):
    shutil.rmtree(path)
    if not re_mkdir:
        os.mkdir(path)
    return True

if __name__ == '__main__':
    print(get_curtime(format_str = "%Y%m%d"))