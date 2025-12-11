# Author   : Dominik Gielarowiec    
# Email    : dgielarowiec@umass.edu
# Spire ID : 35150500

def discriminant(a, b, c):
    return b * b - 4 * a * c

def has_real_root(a, b, c):
    return discriminant(a, b, c) >= 0

def get_real_roots(a, b, c):
    d = discriminant(a, b, c)
    s = d ** 0.5
    return ((-b - s) / (2 * a), (-b + s) / (2 * a))
