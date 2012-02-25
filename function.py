#!/usr/bin/env python
# -*- coding: utf-8 -*-

from commands import getoutput

formula = str(raw_input("Function = \n"))
E = float(raw_input("Epsilon = \n"))
print "Range:"
a = float(raw_input("A = \n"))
b = float(raw_input("B = \n"))

class Function():
    formula = ''
    value = 0.0
    def __init__(self, name, formula, replace, vars):
        self.formula = formula
        i = 0
        while i < len(replace):
            self.formula = self.formula.replace(replace[i], str(vars[i]))
            i = i + 1
        self.value = float(eval(self.formula))
        print name + self.formula + '=' + str(self.value)

def dcount(var):
    rest = var % 1
    i = 0
    while (rest < 1):
        rest = rest * 10
        i = i + 1
    return i
