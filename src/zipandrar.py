# coding=utf-8
import tarfile

import rarfile
import zipfile
from pathlib import Path

from src.basic_opration import *


def unzip_file(file_zip_path, new_zip_dir):
    '''
    解压zip文件，并解决中文文件名乱码的问题
    :param file_zip_path:
    :param new_zip_dir:
    :return: new_unzip_dir： 解压后的路径
    '''
    temp_path = os.path.join(new_zip_dir, 'temp')
    zFile = zipfile.ZipFile(file_zip_path, "r")
    file_lst = zFile.namelist()
    new_unzip_dir = file_lst[0].encode('cp437').decode('gbk')
    if os.path.exists(new_unzip_dir):
        pass
    else:
        for fileM in file_lst:
            extracted_path = Path(zFile.extract(fileM,temp_path))
            # 文件重命名，将中文的文件名还原
            extracted_path.rename(new_zip_dir+'//'+fileM.encode('cp437').decode('gbk'))
        zFile.close()
    return new_unzip_dir

# 解压缩包
def un_rar(orgpath, tarpath):
    after_dir = tarpath
    path, ext = os.path.splitext(orgpath)
    if ext == '.rar':
        with rarfile.RarFile(orgpath) as rf:
            rf.extractall(tarpath)
    elif ext == '.zip':
        after_dir = unzip_file(orgpath, tarpath)
    elif ext == '.tar':
        with tarfile.open('your.tar', 'r') as tar:
            tar.extractall(tarpath)
    else:
        print('Error!')
    return after_dir

def copt_files(basePath, outPath):
    source_path = os.path.abspath(basePath)
    target_path = os.path.abspath(outPath)

    if not os.path.exists(target_path):
        os.makedirs(target_path)

    if os.path.exists(source_path):
        # root 所指的是当前正在遍历的这个文件夹的本身的地址
        # dirs 是一个 list，内容是该文件夹中所有的目录的名字(不包括子目录)
        # files 同样是 list, 内容是该文件夹中所有的文件(不包括子目录)
        for root, dirs, files in os.walk(source_path):
            for file in files:
                src_file = os.path.join(root, file)
                shutil.copy(src_file, target_path)
                print(src_file)
    print('copy files finished!')


if __name__ == '__main__':
    orgpath = 'E:\\test\\FSK_NCBS.rar'
    tarpath = 'E:\\test'
    # un_rar(orgpath, tarpath)
    # copt_files(orgpath, tarpath)
    file_zip_path = 'D:\FREM_ZIP\\20210223\\FERM20-平台基础升级包(基于V202101-0-0)_V202101-1-0V202102230322.zip'
    new_zip_dir = 'D:\FREM_ZIP\\20210223\\'
    unzip_file(file_zip_path, new_zip_dir)