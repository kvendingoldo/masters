from numpy import linalg
from padic.padic import *
import copy

A = [[PAdic("1", 5), PAdic("0", 5)], [PAdic("0", 5), PAdic("1", 5)]]
B = [PAdic("2", 5),PAdic("3", 5)]
C = copy.deepcopy(A)
X = []

for i in range(0, len(B)):
    for j in range(0, len(B)):
        C[j][i] = B[j]
        if i > 0:
            C[j][i - 1] = A[j][i - 1]
    X.append(linalg.det(C) / linalg.det(A), 1)

print('w=%s' % X[0], 'x=%s' % X[1])
#, 'y=%s' % X[2], 'z=%s' % X[3])
#print(determinant_recursive([[PAdic("1", 5), PAdic("0", 5)], [PAdic("0", 5), PAdic("3", 5)]]))
