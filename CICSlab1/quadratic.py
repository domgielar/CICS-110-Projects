# Author   : Dominik Gielarowiec
# Email    : dgielarowiec@umass.edu
# Spire ID : 35150500

import math

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

quadratic1 = (-b+(math.sqrt((b**2)-4*a*c)))/(2*a)
quadratic2 = (-b-(math.sqrt((b**2)-4*a*c)))/(2*a)

print(f"{a}*x^2+{b}*x+{c} has roots: \n1. {quadratic1} \n2. {quadratic2}" )