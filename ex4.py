# -*- coding: utf-8 -*-
cars = 100
space_in_a_car = 4.0
# space_in_a_car = 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

# 如果乘客数不能整除，比如将90改为95人， 则有的需要每辆坐3人，有的需要每辆坐4人， 以后设计语句自动计算并输出几辆坐3人，几辆坐4人。

print u"下面是更多的练习"
print "--------------------"

print "Hey %s there." % "you"

name = "Wentao"
print "My name is %s." % name

print "My name is %s." % name+"Sun"

x = 0
y = 10
i = 9

print i + (x + y) / 2
