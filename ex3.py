# -*- coding: utf-8 -*-
print "I will now count my chickens:" # 说明性语句

print "Hens", 25 + 30 /6 # 输入公式可以直接输出结果， 后面尝试下 31 / 6 和 31.0 / 6.0 ,注意浮点数
print "Roosters", 100 - 25 * 3 % 4 # % 是用来取余的

print "Now I will count the eggs:" # 说明性语句

print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6 #注意计算运算优先级，PEMDAS-扩指乘除加减，尝试 1 - 5 + 4是否为-8

print "Is it true that 3 + 2 < 5 - 7?" #说明性语句

print 3 + 2 < 5 - 7 # 逻辑判断语句，直接输出True、False

print "What is 3 + 2?", 3 + 2
print "What is 5 - 7?", 5 - 7

print "Oh, that's why it's False."

print "How about some more."

print "Is it greater?", 5 > -2
print "Is it greater or equal?", 5 >= -2
print "Is it less or equal?", 5 <= -2
print u"欧耶，再次成功！" # 输入中文字符，记得首行语句和在print后加u""

print u"下面是附加练习"
print "------------------------"
print "What is 1 - 5 + 8", 1 - 5 + 8 #加减平级看左右
print "What is 4 / 2 * 2", 4 / 2 * 2 #乘除平级看左右
print u"1等于1吗？", 1 == 1 # 赋值是=，等于是==
print u"1等于1.0吗？", 1 == 1.0 # 精确不同的位数与数据本身的大小无关
print u"1等于1.00吗？", 1 == 1.00
print u"1不等于1吗？", 1 <> 1
print u"5等于3+2吗？", 5 == 3 + 2
print u"5不等于3+2吗？", 5 <> 3 + 2
# print Sin(Pi/2) #尝试计算三角函数
print 31 / 6 # 取整
print 31 % 6 #取余
print round(31/6) # 四舍五入
print 31.0 / 6 #浮点数
print 31 / 6.0 #浮点数
print 31.0 / 6.0 #浮点数
