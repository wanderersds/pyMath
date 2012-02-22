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




#a=b=1
#c = Function('C=', 'a+(b-a)/2.0', ['a'], [b])
#
#class cFunction(Function):
#    def __init__(self, a, b):1111
#        self.formula = str(a) + '+(' + str(b) + '-' + str(a) + ')/2.0'
#        self.value = a+(b-a)/2.0
#        print "C=" + self.formula + '=' + str(self.value)

#class c2Function(Function):
#
#    def __init__(self, a , b, Fa, Fb):
#        self.value = (a-((b-a)/(Fb.value-Fa.value))*Fa.value)
#        self.formula = str(a) + '-((' + str(b) + '-' + str(a) + ')/(' + str(Fb.value) + '-' + str(Fa.value) + '))*' + str(Fa.value)
#        print "C=" + self.formula + '=' + str(self.value)
#
#        a-((b-a)/(Fb-Fa))*Fa
#
