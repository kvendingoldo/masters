# -*- coding: utf-8 -*-
# @Author: Alexander Sharov

import random
from padic import *

N = 10
n = 3
base = 5


def generate():
    A = Matrix(n, n)
    for i in range(0, n, 1):
        row = []
        for j in range(0, n, 1):
            if i == j:
                row.append(PAdic("10", base))
            else:
                number = abs(1 - random.randrange(N) * round((i - j)) ** 2)
                row.append(PAdic(str(number), base))
        A[i] = row
    return A
