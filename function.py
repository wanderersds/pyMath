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

    def formulate(self, symbol, other):
        self.formula = '(' + self.formula + ')' + symbol + '(' + other.formula + ')'

    def __init__(self, name, formula, replace, vars):
        self.formula = formula
        i = 0
        while i < len(replace):
            self.formula = self.formula.replace(replace[i], str(vars[i]))
            i = i + 1
        self.value = float(eval(self.formula))
        print name + self.formula + '=' + str(self.value)

    def __float__(self):
        return self.value

    def __add__(self, other):
        self.formulate('+', other)
        self.value = self.value + other.value

    def __sub__(self, other):
        self.formulate('-', other)
        self.value = self.value - other.value

    def __mul__(self, other):
        self.formulate('*', other)
        self.value = self.value * other.value

    def __div__(self, other):
        self.formulate('/', other)
        self.value = self.value / other.value

    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self.value <= other.value

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return self.value != other.value

    def __gt__(self, other):
        return self.value > other.value

    def __ge__(self, other):
        return self.value >= other.value


def dcount(var):
    rest = var % 1
    i = 0
    while (rest < 1):
        rest = rest * 10
        i = i + 1
    return i
