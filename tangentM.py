#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
from function import *

r = re.compile('\-?[0-9]+')
Ax, Bx, Cx = r.findall(formula)

Fa = Function('F(a)', formula, ['x'], [a])
Fb = Function('F(b)', formula, ['x'], [b])

if (Fa > Fb):
    print 'F(x) спадает.'
    print "F'= 2*"+ Ax +"*x+"+ Bx + "= 0"
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

Fz = Function('F(z)', formula, ['x'], [z])
Fzi= Function("F'(z)", "2*Ax*z+Bx", ["Ax", "Bx", "z"], [float(Ax), float(Bx), z])

delta = E
delta_prev_prev = delta_prev = 0

while (True):
    delta_prev_prev = delta_prev
    delta_prev = delta
    c_begin = Function('Cbeg', 'z - (Fz/Fzi)', ["Fzi", "Fz","z"], [Fzi, Fz, z])
    Fa = Function('F(a)', formula, ['x'], [a])
    Fb = Function('F(b)', formula, ['x'], [b])
    Fc = Function('F(c)', formula, ['x'], [c_begin])
    if (Fc > 0 and Fa > 0) or (Fc < 0 and Fa < 0):
        a = c_begin
        print "F(c) и F(a) имеют один знак. (A=C)"
    else:
        b = c_begin
        print "F(c) и F(b) имеют один знак. (B=C)"
    Fci= Function("F'(c)", "2*Ax*c+Bx", ["Ax", "Bx","c"], [float(Ax), int(Bx), c_begin])
    c_end = Function('Cend', 'c_begin - (Fc/Fci)', ["c_begin","Fci", "Fc"], [c_begin, Fci, Fc])
    z = c_end
    Fz = Fc
    Fzi = Fci
    delta = abs(c_begin - c_end)
    if (not (delta >= E and delta != delta_prev and delta_prev != delta_prev_prev)): break

print "C=" + c_end.formula + '=' + str(c_end.value) #Старый формат, переписать
print round(c_end, dcount(E))
