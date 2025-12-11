# Author   : Dominik Gielarowiec    
# Email    : dgielarowiec@umass.edu
# Spire ID : 35150500

import math

def cullen(n):
    return n * (2 ** n) + 1

def woodall(n):
    return n * (2 ** n) - 1

def fermat(n):
    return 2 ** (2 ** n) + 1

def divides_evenly(dividend, divisor):
    return dividend % divisor == 0

def cone_volume(r, h):
    return math.pi * (r * r) * (h / 3)
