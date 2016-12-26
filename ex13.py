# -*- coding: utf-8 -*-
#from sys import argv

#script, first, second, third = argv

#print "The script is called:", script
#print "Your first variable is:", first
#print "Your second variable is:", second
#print "Your third variable is:", third

print u"下面自己编写新的脚本"

from sys import argv

script, population, epi_data, diag_rate, treat_rate, first_line_rate, second_line_rate, mkt_share = argv

script = "Patients for sales calculation model"
population = raw_input("What's the total population?")
epi_data = raw_input("What's the prevelence of the indication?")
diag_rate = raw_input("What's the diagozed rate?")
treat_rate = raw_input("What's the treatment rate?")
first_line_rate = raw_input("What's the first line rate?")
second_line_rate = raw_input("What's the second line rate?")
mkt_share = raw_input("What's the market share?")

a = float( population ) 
b = float( epi_data ) / 100000
c = float( diag_rate)
d = float( treat_rate )
e = float( first_line_rate )
f = float( second_line_rate )
g = float( mkt_share )

print "The script is called: %r" % script
print "The patients in market is %d" % (a * b * c * d * e * f * g)
