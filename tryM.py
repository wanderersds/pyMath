#!/usr/bin/env python
# -*- coding: utf-8 -*-

from function import *

c = Function('C', 'a+(b-a)/2.0', ['a', 'b'], [a, b])

while (abs(a-b) > E):
    print "Delta(C)" + '|' + str(b) + '-' + str(a) + '|' + '=' + str(abs(b-a))
    Fa = Function('F(a)', formula, ['x'], [a])
    Fb = Function('F(b)', formula, ['x'], [b])
    Fc = Function('F(c)', formula, ['x'], [c])
    if (Fc > 0 and Fa > 0) or (Fc < 0 and Fa < 0):
        a=c
        print "F(c) и F(a) имеют один знак. (A=C)"
    else:
        b=c
        print "F(c) и F(b) имеют один знак. (B=C)"
    c = Function('C', 'a+(b-a)/2.0', ['a', 'b'], [a, b])

print round(c, dcount(E))
