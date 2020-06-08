# -*- coding: utf-8 -*-
# @Author: Alexander Sharov

import numpy as np


def symm_matrix(N):
    '''Generates a Random Real Symmetric Matrix of dimensions NxN'''
    A = np.zeros([N, N])
    for i in range(N):
        for j in range(i + 1):
            A[i, j] = np.random.random()
            A[j, i] = A[i, j]
    return A
