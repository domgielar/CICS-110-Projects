# Author   : Dominik Gielarowiec    
# Email    : dgielarowiec@umass.edu
# Spire ID : 35150500


from logic import nand, implies, iff, xor

def nand_of_tuple(t):
    return nand(t[0], t[1])

def implies_in_both_directions(lst):
    a, b = lst[0], lst[1]
    lst[0] = implies(a, b)
    lst[1] = implies(b, a)
    return lst

def iff_with_result(lst):
    lst.append(iff(lst[0], lst[1]))
    return lst

def xor_with_result_in_between(lst):
    lst.insert(1, xor(lst[0], lst[1]))
    return lst
