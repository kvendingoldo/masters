import datetime
from padic.padic import *
from padic.matrix import *

p1 = PAdic("1/13", 101)
p2 = PAdic("13", 101)
print(str(p1))
print(str(p2))

print("add")
print(str(p1+p2))


print("sub")
print(str(p1-p2))

print("mul")
print(str(p1*p2))

print("divide")
print(str(p1/p2))

#print("neg")
#print(str(-PAdic("1/2", 5)))

#m1 = Matrix(2, 2)
#m2 = Matrix(2, 2)

#m1[0] = [PAdic("1", 7),PAdic("4", 7)]
#m1[1] = [PAdic("0", 7),PAdic("3", 7)]


#m2[0] = [PAdic("5", 2),PAdic("6", 2)]
#m2[1] = [PAdic("7", 2),PAdic("8", 2)]

#m3 = m1 + m2
#m4 = m1 - m2
#m5 = m1 * m2

#print(m3)
#print(m4)
#print(datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S_%f"))
#print(Matrix.determinant(m1))
#print(datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S_%f"))


#p2 = -(PAdic("1", 5))
#print(p2)