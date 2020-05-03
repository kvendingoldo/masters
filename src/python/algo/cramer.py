# -*- coding: utf-8 -*-
# @Author: Alexander Sharov

from padic.padic import *
from padic.matrix import *
import copy


def cramer(A, b):
    C = copy.copy(A)
    b_len = len(b)
    X = []

    for i in range(0, b_len):
        for j in range(0, b_len):
            C[j][i] = b[j]
            if i > 0:
                C[j][i - 1] = A[j][i - 1]
        print(type(C))
        X.append(Matrix.determinant(C))
    return X
