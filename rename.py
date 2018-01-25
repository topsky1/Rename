import os

new_name = input("请输入要更改的新文件名：")

num = 1
for x in os.listdir('.'):
    if x[0] != '.' and x != 'rename.py':
        xx = new_name + str(num) + os.path.splitext(x)[1]
        os.rename(x, xx)
