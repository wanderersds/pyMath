#!/usr/bin/env python
# -*- coding: utf-8 -*-

from commands import getoutput

class Function():
    formula = ''
    value = 0.0
    def __init__(self, x, name, formula):
        self.formula = formula.replace('x', str(x))
        self.value = float(eval(self.formula))
        print name + self.formula + '=' + str(self.value)


class cFunction(Function):
    def __init__(self, a, b):
        self.formula = str(a) + '+(' + str(b) + '-' + str(a) + ')/2.0'
        self.value = a+(b-a)/2.0
        print "C=" + self.formula + '=' + str(self.value)

class c2Function(Function):

    def __init__(self, a , b, Fa, Fb):
        self.value = (a-((b-a)/(Fb.value-Fa.value))*Fa.value)
        self.formula = str(a) + '-((' + str(b) + '-' + str(a) + ')/(' + str(Fb.value) + '-' + str(Fa.value) + '))*' + str(Fa.value)
        print "C=" + self.formula + '=' + str(self.value)
