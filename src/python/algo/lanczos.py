# -*- coding: utf-8 -*-
# @Author: Alexander Sharov

import numpy as np
from scipy.linalg import norm, solve
from numpy.linalg import qr


def IPI(A, maxiter=1000, tol=1E-06):
    '''Obtain smallest eigenvalue and corresponding eigenvector via Inverse Power Iteration with Shift'''
    n = A.shape[0]

    x = np.ones(n)
    s = -3000
    B = A - s * np.identity(n)
    for j in range(1, maxiter):
        u = x / norm(x)
        x = solve(B, u)
        mu = u.T @ x

    lam = 1 / mu + s
    return (lam)


def LanczosTri(A):
    '''Tridiagonalize Matrix A via Lanczos Iterations'''

    if ((A.transpose() != A).all()):
        print("WARNING: Input matrix is not symmetric")
    n = A.shape[0]
    x = np.ones(n)
    V = np.zeros(n * n).reshape(n, n)
    # Begin Lanczos Iteration
    q = x / np.linalg.norm(x)
    V[:, 0] = q
    r = A @ q
    a1 = q.T @ r
    r = r - a1 * q
    b1 = norm(r)
    s_min = 0
    for j in range(2, n + 1):
        v = q
        q = r / b1
        V[:, j - 1] = q
        r = A @ q - b1 * v
        a1 = q.T @ r
        r = r - a1 * q
        b1 = norm(r)
        if b1 == 0:
            break

    T = V.T @ A @ V

    alpha = norm(T) / norm(A)
    T = T / alpha

    return T
