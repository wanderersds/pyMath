#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import string
#from function import *

formula = str(raw_input("Function = \n"))
E = float(raw_input("Epsilon = \n"))
print "Range:"
a = float(raw_input("A = \n"))
b = float(raw_input("B = \n"))

class Function:
    formula = ''
    value = 0.0
    def __init__(self, name, formula, replace, vars):
        i = 0
        while i < len(replace):
            formula = formula.replace(replace[i], str(vars[i]))
            i = i + 1
        self.formula = formula
        self.value = float(eval(self.formula))
        print name + self.formula + '=' + str(self.value)

def dcount(var):
    rest = var % 1
    i = 0
    while (rest < 1):
        rest = rest * 10
        i = i + 1
    return i

r = re.compile('\-?[0-9]+')
Ax, Bx, Cx = r.findall(formula)

Fa = Function('F(a)=', formula, ['x'], [a])
Fb = Function('F(b)=', formula, ['x'], [b])

if (Fa.value > Fb.value):
    print 'F(x) спадает.'
    print "F'= 2*"+ Ax +"*x+"+ Bx + "= 0"
    #Fi = Function("F'=", "2*Ax*x+Bx", ["Ax", "Bx"], [Ax, Bx]) #test
    #Fii = Function("F''=", "Bx", ["Bx"], [Bx])
    if (int(Bx) > 0):
        print "F''= "+Bx+' > 0'
        z = a
    else:
        print "F''= "+Bx+' < 0'
        z = b
else:
    print 'F(x) растет.'
    print "F'= 2*"+ Ax + "*x+"+ Bx + "= 0"
    if (int(Bx) > 0):
        print "F''= "+Bx+' > 0'
        z = b
    else:
        print "F''= "+Bx+' < 0'
        z = a

Fz = Function('F(z)=', formula, ['x'], [z])
Fzi= Function("F'(z)=", "2*Ax*z+Bx", ["Ax", "Bx", "z"], [float(Ax), float(Bx), z])

delta = E
delta_prev_prev = delta_prev = 0

while (True):
    delta_prev_prev = delta_prev
    delta_prev = delta
    c_begin = Function('Cbeg=', 'z - (Fz.value/Fzi.value)', ["Fz.value", "Fzi.value","z"], [Fz.value, Fzi.value, z])
    Fa = Function('F(a)=', formula, ['x'], [a])
    Fb = Function('F(b)=', formula, ['x'], [b])
    Fc = Function('F(c)=', formula, ['x'], [c_begin.value])
    if (Fc.value > 0 and Fa.value > 0) or (Fc.value < 0 and Fa.value < 0):
        a = c_begin.value
        print "F(c) и F(a) имеют один знак. (A=C)"
    else:
        b = c_begin.value
        print "F(c) и F(b) имеют один знак. (B=C)"
    Fci= Function("F'(c)=", "2*Ax*c+Bx", ["Ax", "Bx","c"], [float(Ax), int(Bx), c_begin.value])
    c_end = Function("Cend=", 'c_begin.value - (Fc.value/Fci.value)', ["c_begin.value","Fc.value", "Fci.value"], [c_begin.value, Fc.value, Fci.value])
    z = c_end.value
    Fz = Fc
    Fzi = Fci
    delta = abs(c_begin.value - c_end.value)
    if (not (delta >= E and delta != delta_prev and delta_prev != delta_prev_prev)): break

print "C=" + c_end.formula + '=' + str(c_end.value)

print round(c_end.value, dcount(E))
