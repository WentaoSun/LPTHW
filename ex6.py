# -*- coding: utf-8 -*-
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x # %r 代替整体引用原始数据
print "I also said: '%s'." % y # %s 在此显示变量

hilarious = False
joke_evaluation = "Is't that joke so funny?! %r"

print joke_evaluation % hilarious # 相当于print "Is't that joke so funny?! %r" % hilarious

w = "This is the left side of ..."
e = "a string with a right side."

print w + e # +在这里起到的作用是把两个字符串相连。

print u"习题6完成"
