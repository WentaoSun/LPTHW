# -*- coding: utf-8 -*-
from sys import argv #sys 是一个软件包, argv 是它的一个模块, 存储参数变量,将 python 中参数变量的模块引入脚本

script, filename = argv #将 argv 解包,赋值到左边的两个变量,这也是获得文件名的方法

txt = open(filename) # open 函数返回的是一个叫"file object"的东西txt,可以随意访问内容的任意位置,然后读取这些内容, 但这个文件本身不是内容.

print "Here's your file %r:" % filename #常见的文件名打印
print txt.read() # 对 txt 这个文件执行读取命令,并把内容打印出来

txt.close()

print "Type the filename again:" # 要求再次打印文件名
file_again = raw_input("> ") # 在提示符> 后手工键入上一条语句要求的内容

txt_again = open(file_again) # 再次返回文件

print txt_again.read() # 再次打印文件内容

txt_again.close()




