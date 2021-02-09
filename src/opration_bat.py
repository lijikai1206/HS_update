#coding:utf-8
import os

#bat文件的内容(temp.bat)
bat_name='temp.bat'
s1='''echo off
ipconfig
echo Hello world!
echo show %1%
set Pan=c:\\abc
C:
CD \\
if NOT exist %Pan% (md abc)
'''

#写入一个临时文件
with open('e:\\'+bat_name,'w') as f:
    f.write(s1)


#执行BAT并定向输入(不出现黑窗口)
import subprocess
cmd = 'cmd.exe E:\\'+bat_name
#其中input_var是输入参数变量
p = subprocess.Popen("cmd.exe /c" + "E:\\"+bat_name+" input_var", stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
curline = p.stdout.readline()
while(curline != b''):
    if len(curline)>2:
        print(curline.decode('gbk'))
        curline = p.stdout.readline()

p.wait()

os.chdir('E:\\')
os.remove('temp.bat')