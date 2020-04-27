from padic import *

p1 = PAdic("1/2", 5)
p2 = PAdic("1/3", 5)
print(str(p1))
print(str(p2))

print("add")
print(str(PAdic("1/2", 5) + PAdic("1/3", 5)))

print("sub")
print(str(PAdic("1/2", 5) - PAdic("1/3", 5)))

print("mul")
print(str(PAdic("1/2", 5) * PAdic("1/3", 5)))

print("divide")
print(str(PAdic("1/2", 5) / (PAdic("1/3", 5))))



print("neg")
print(str(-PAdic("1/2", 5)))