#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
import string
from commands import getoutput

formula=''

class Function():
    global formula
    formula_x = formula
    value = 0
    def __init__(self, x, x_name):
        self.formula_x = formula.replace('x', str(x))
        self.value = float(getoutput("./bccalc.sh " + "'" + self.formula_x + "'"))
        print "F(" + x_name + ")=" + self.formula_x + '=' + str(self.value)    

class cFunction(Function):
    formula_x = "a+(b-a)/2"
    def __init__(self, a, b):
        self.fromula_x = formula.replace('a',str(a))
        self.formula_x = formula.replace('b',str(b))
        self.value=a+(b-a)/2.0
        print "C=" + str(self.formula_x) + '=' + str(self.value)


formula = str(raw_input("Function: "))
print "Range"
print "A:"
a = float(input())
print "B:"
b = float(input())


c=cFunction(a,b)

while (abs(b-a) > 0.1):
    print "Delta(C)=" + '|' + str(b) + '-' + str(a) + '|' + '=' + str(abs(b-a))
    Fa=Function(a,'a')
    Fb=Function(b,'b')
    Fc=Function(c.value,'c')
    if (Fc.value > 0 and Fa.value > 0) or (Fc.value < 0 and Fa.value < 0):
        a=c.value
        print "F(c) and F(a) having the same sign. (A=C)"
    else: 
        b=c.value
        print "F(c) and F(a) having the same sign. (B=C)" 
    c=cFunction(a,b)

print "C=" + c.formula_x + '=' + str(c.value)
print round(c.value,1)
