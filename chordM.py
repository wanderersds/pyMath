#!/usr/bin/env python
# -*- coding: utf-8 -*-

import string
from function import *

while (True):
    Fa = Function('F(a)=', formula, ['x'], [a])
    Fb = Function('F(b)=', formula, ['x'], [b])
    c_begin = Function('C=', 'a-((b-a)/(Fb-Fa))*Fa', ['Fa', 'Fb', 'a', 'b'], [Fa.value, Fb.value, a, b])
    Fc = Function('F(c)=', formula, ['x'], [c_begin.value])
    if (Fc.value > 0 and Fa.value > 0) or (Fc.value < 0 and Fa.value < 0):
        a = c_begin.value
        print "F(c) и F(a) имеют один знак. (A=C)"
    else:
        b = c_begin.value
        print "F(c) и F(b) имеют один знак. (B=C)"
    c_end = Function('C=', 'a-((b-a)/(Fb-Fa))*Fa', ['Fa', 'Fb', 'a', 'b'], [Fa.value, Fb.value, a, b])
    print "Delta(c)=" + '|' + str(c_begin.value) + '-' + str(c_end.value) + '|=' + str(abs(c_begin.value-c_end.value))
    if (abs(c_begin.value - c_end.value) <= E): break

print "C=" + c_end.formula + '=' + str(c_end.value)

print round(c_end.value, dcount(E))
