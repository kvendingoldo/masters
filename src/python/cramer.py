from numpy import linalg
from padic.padic import *
from padic.matrix import *
import copy

n = 3
A = Matrix(n, n)
B = [PAdic("2", 5), PAdic("3", 5), PAdic("3", 5)]

for i in range(0, n, 1):
    row = []
    for j in range(0, n, 1):
        if i == j:
            row.append(PAdic("10", 5))
        else:
            number = round(1 - (i - j) ** 2 / n)
            row.append(PAdic(str(number), 5))
    A[i] = row


C = copy.copy(A)

X = []

for i in range(0, len(B)):
    for j in range(0, len(B)):
        C[j][i] = B[j]
        if i > 0:
            C[j][i - 1] = A[j][i - 1]
    print(type(C))
    X.append(Matrix.determinant(C))#/ Matrix.determinant(A))

print('w=%s' % X[0], 'x=%s' % X[1])
# , 'y=%s' % X[2], 'z=%s' % X[3])
# print(determinant_recursive([[PAdic("1", 5), PAdic("0", 5)], [PAdic("0", 5), PAdic("3", 5)]]))
