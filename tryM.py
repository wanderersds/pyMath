#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
import string
from function import *

#formula = str(raw_input("Function: "))
print "Function = "
formula = str(raw_input())
print "Epsilon = "
E = float(input())
print "Range:"
print "A = "
a = float(input())
print "B = "
b = float(input())

c=cFunction(a,b)

while (abs(b-a) > E):
    print "Delta(C)=" + '|' + str(b) + '-' + str(a) + '|' + '=' + str(abs(b-a))
    Fa = Function(a,'F(a)=',formula)
    Fb = Function(b,'F(b)=',formula)
    Fc = Function(c.value, 'F(c)=', formula)
    if (Fc.value > 0 and Fa.value > 0) or (Fc.value < 0 and Fa.value < 0):
        a=c.value
        print "F(c) and F(a) having the same sign. (A=C)"
    else:
        b=c.value
        print "F(c) and F(a) having the same sign. (B=C)"
    c=cFunction(a,b)

print "C=" + c.formula + '=' + str(c.value)

print round(c.value, len(str(E))-2)
