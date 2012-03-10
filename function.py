#!/usr/bin/env python
# -*- coding: utf-8 -*-

formula = str(raw_input("Function = \n"))
E = float(raw_input("Epsilon = \n"))
print "Range:"
a = float(raw_input("A = \n"))
b = float(raw_input("B = \n"))

class Function:
    formula = ''
    value = 0.0
    name = ''
    def __repr__(self):
        return self.name + '='+ self.formula + '=' + str(self.value)

    def __init__(self, name, formula, replace = [], vars = []):
        self.formula = formula
        self.name = name
        i = 0
        while i < len(replace):
            self.formula = self.formula.replace(replace[i], str(vars[i]))
            i = i + 1
        self.value = float(eval(self.formula))
        print self.__repr__()

    def __float__(self):
        return self.value

    def __str__(self):
        return self.formula

    def formulate(self, symbol, other):
        if (type(other) in [float, int]):
            other = float(other)
            return Function(self.name + symbol + str(other), '(' + self.formula + ')' + symbol + '(' + str(other) + ')')
        elif (type(other) == type(self)):
            return Function(self.name + symbol + other.name, '(' + self.formula + ')' + symbol + '(' + str(other) + ')')
        else:
            raise TypeError("undefined addition: %s, %s" % (type(self), type(other)))

    def __add__(self, other):
        self.formulate('+', other)

    def __sub__(self, other):
        self.formulate('-', other)

    def __mul__(self, other):
        self.formulate('*', other)

    def __div__(self, other):
        self.formulate('/', other)

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


def dcount(var):
    rest = var % 1
    i = 0
    while (rest < 1):
        rest = rest * 10
        i = i + 1
    return i
