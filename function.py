#!/usr/bin/env python
# -*- coding: utf-8 -*-

from commands import getoutput

class Function():
    formula = ''
    value = 0.0
    def __init__(self, x, name, formula):
        self.formula = formula.replace('x', str(x))
        self.value = float(getoutput("./bccalc.sh " + "'" + self.formula + "'"))
        print "F(" + name + ")=" + self.formula + '=' + str(self.value)

    def __float__(self):
		return self.value

class cFunction(Function):
    def __init__(self, a, b):
        self.formula = str(a) + '+(' + str(b) + '-' + str(a) + ')/2.0'
        self.value = a+(b-a)/2.0
        print "C=" + str(self.formula) + '=' + str(self.value)
