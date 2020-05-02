from padic.padic import *
from padic.matrix import *

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

m1 = Matrix(2, 2)
#m2 = Matrix(2, 2)

m1[0] = [PAdic("1", 5),PAdic("0", 5)]
m1[1] = [PAdic("0", 5),PAdic("4", 5)]

#m2[0] = [PAdic("5", 2),PAdic("6", 2)]
#m2[1] = [PAdic("7", 2),PAdic("8", 2)]

#m3 = m1 + m2
#m4 = m1 - m2
#m5 = m1 * m2

#print(m3)
#print(m4)
print(Matrix.determinant(m1))
