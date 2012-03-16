#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Function(object):
    formula = ''
    value = 0.0
    name = ''

    def __init__(self, name, formula, replace = [], vars = []):
        self.formula = formula
        self.name = name
        i = 0
        while i < len(replace):
            self.formula = self.formula.replace(replace[i], str(float(vars[i])))
            i = i + 1
        self.value = float(eval(self.formula))
        print self.name + '='+ self.formula + '=' + str(self.value)

    def __float__(self):
        return self.value

    def __str__(self):
        return self.formula

    def formulate(self, symbol, other):
        if (type(other) in [int, float]):
            other = float(other)
            return Function(self.name + symbol + str(other), '(' + self.formula + ')' + symbol + '(' + str(other) + ')')
        elif (type(other) == type(self)):
            return Function(self.name + symbol + other.name, '(' + self.formula + ')' + symbol + '(' + str(other) + ')')
        else:
            raise TypeError("undefined addition: %s, %s" % (type(self), type(other)))

    def __add__(self, other):
        return self.formulate('+', other)

    def __sub__(self, other):
        return self.formulate('-', other)

    def __mul__(self, other):
        return self.formulate('*', other)

    def __div__(self, other):
        return self.formulate('/', other)

    def __mod__(self, other):
        return self.formulate('%', other)

    def __abs__(self):
        return Function('abs(' + self.name + ')', 'abs(' + self.formula + ')')

    def __lt__(self, other):
        return self.value < other

    def __le__(self, other):
        return self.value <= other

    def __eq__(self, other):
        return self.value == other

    def __ne__(self, other):
        return self.value != other

    def __gt__(self, other):
        return self.value > other

    def __ge__(self, other):
        return self.value >= other

    __radd__=__add__
    __rsub__=__sub__
    __rmul__=__mul__
    __rdiv__=__div__
    __rmod__=__mod__
    __rabs__=__abs__
    __rlt__=__lt__
    __rle__=__le__
    __req__=__eq__
    __rne__=__ne__
    __rgt__=__gt__
    __rge__=__ge__


def dcount(var):
    rest = var % 1
    i = 0
    while (rest < 1):
        rest = rest * 10
        i = i + 1
    return i

formula = str(raw_input("Function = \n"))
E = float(raw_input("Epsilon = \n"))
print "Range:"
a = float(raw_input("A = \n"))
b = float(raw_input("B = \n"))

