from padic.padic import *
from padic.matrix import *
import copy


def cramer(A, B):
    C = copy.copy(A)
    B_len = len(B)
    X = []

    for i in range(0, B_len):
        for j in range(0, B_len):
            C[j][i] = B[j]
            if i > 0:
                C[j][i - 1] = A[j][i - 1]
        print(type(C))
        X.append(Matrix.determinant(C))
    return X
