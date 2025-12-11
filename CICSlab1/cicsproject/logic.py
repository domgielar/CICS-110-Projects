# Author   : Dominik Gielarowiec    
# Email    : dgielarowiec@umass.edu
# Spire ID : 35150500

def nand(A, B):
    return not (A and B)

def implies(A, B):
    return (not A) or B

def iff(A, B):
    return (A and B) or ((not A) and (not B))

def xor(A, B):
    return (A and (not B)) or ((not A) and B)
