#!/usr/bin/env python
# -*- coding: utf-8 -*-

from function import *

while (True):
    Fa = Function('F(a)', formula, ['x'], [a])
    Fb = Function('F(b)', formula, ['x'], [b])
    c_begin = Function('C', 'a-((b-a)/(Fb-Fa))*Fa', ['Fa', 'Fb', 'a', 'b'], [Fa, Fb, a, b])
    Fc = Function('F(c)=', formula, ['x'], [c_begin])
    if (Fc > 0 and Fa > 0) or (Fc < 0 and Fa < 0):
        a = c_begin
        print "F(c) и F(a) имеют один знак. (A=C)"
    else:
        b = c_begin
        print "F(c) и F(b) имеют один знак. (B=C)"
    c_end = Function('C=', 'a-((b-a)/(Fb-Fa))*Fa', ['Fa', 'Fb', 'a', 'b'], [Fa, Fb, a, b])
    DeltaC = Function('Delta(C)', 'abs(c_begin-c_end)', ['c_begin', 'c_end'], [c_begin, c_end])
    if (DeltaC <= E): break

print "C=" + c_end.formula + '=' + str(c_end.value)
print round(c_end, dcount(E))
