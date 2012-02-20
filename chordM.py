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
while (True):

    Fa = Function(a,'F(a)=',formula)
    Fb = Function(b,'F(b)=',formula)
    c_begin = c2Function(a, b, Fa, Fb)
    Fc = Function(c_begin.value, 'F(c)=', formula)
    if (Fc.value > 0 and Fa.value > 0) or (Fc.value < 0 and Fa.value < 0):
        a=c_begin.value
        print "F(c) and F(a) having the same sign. (A=C)"
    else:
        b=c_begin.value
        print "F(c) and F(a) having the sme sign. (B=C)"
    c_end = c2Function(a, b, Fa, Fb)
    print "Delta(c)=" + '|' + str(c_begin.value) + '-' + str(c_end.value) + '|=' + str(abs(c_begin.value-c_end.value))
    if (abs(c_begin.value - c_end.value) <= E): break

print "C=" + c_end.formula + '=' + str(c_end.value)

print round(c_end.value, len(str(E))-2)
