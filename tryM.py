#!/usr/bin/env python
# -*- coding: utf-8 -*-

from function import *

c = Function('C=', 'a+(b-a)/2.0', ['a', 'b'], [a, b])

while (abs(b-a) > E):
    print "Delta(C)=" + '|' + str(b) + '-' + str(a) + '|' + '=' + str(abs(b-a))
    Fa = Function('F(a)=', formula, ['x'], [a])
    Fb = Function('F(b)=', formula, ['x'], [b])
    Fc = Function('F(c)=', formula, ['x'], [c.value])
    if (Fc > 0 and Fa > 0) or (Fc.value < 0 and Fa.value < 0):
        a=c.value
        print "F(c) и F(a) имеют один знак. (A=C)"
    else:
        b=c.value
        print "F(c) и F(b) имеют один знак. (B=C)"
    c = Function('C=', 'a+(b-a)/2.0', ['a', 'b'], [a, b])

print round(c.value, dcount(E))
