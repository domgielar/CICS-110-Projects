# Author   : Dominik Gielarowiec
# Email    : dgielarowiec@umass.edu
# Spire ID : 35150500

dividend = int(input("What is the dividend:"))
divisor = int(input("What is the divisor:"))

amt = int(dividend/divisor)
remainder = dividend%divisor

print(f"{dividend}/{divisor} equals:\n\t{amt} and {remainder}/{divisor}")