#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
import string
from function import *

formula = str(raw_input("Function: "))
print "Range"
print "A:"
a = float(input())
print "B:"
b = float(input())

c=cFunction(a,b)

while (abs(b-a) > 0.1):2
    print "Delta(C)=" + '|' + str(b) + '-' + str(a) + '|' + '=' + str(abs(b-a))
    Fa = Function(a,'a',formula)
    Fb = Function(b,'b',formula)
    Fc = Function(c.value, 'c', formula)
    if (Fc.value > 0 and Fa.value > 0) or (Fc.value < 0 and Fa.value < 0):
        a=c.value
        print "F(c) and F(a) having the same sign. (A=C)"
    else:
        b=c.value
        print "F(c) and F(a) having the same sign. (B=C)"
    c=cFunction(a,b)

print "C=" + c.formula + '=' + str(c.value)
print round(c,1)