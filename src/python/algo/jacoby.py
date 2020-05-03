# -*- coding: utf-8 -*-
# @Author: Alexander Sharov

from math import sqrt


def max_elem(a):
    n = len(a)
    a_max = 0.0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if abs(a[i][j]) >= a_max:
                a_max = abs(a[i][j])
                k = i
                l = j
    return a_max, k, l


def rotate(a, p, k, l):
    n = len(a)
    aDiff = a[l][l] - a[k][k]
    if abs(a[k][l]) < abs(aDiff) * 1.0e-36:
        t = a[k][l] / aDiff
    else:
        phi = aDiff / (2.0 * a[k][l])
        t = 1.0 / (abs(phi) + sqrt(phi ** 2 + 1.0))
        if phi < 0.0:
            t = -t
    c = 1.0 / sqrt(t ** 2 + 1.0)
    s = t * c
    tau = s / (1.0 + c)
    temp = a[k][l]
    a[k][l] = 0.0
    a[k][k] = a[k][k] - t * temp
    a[l][l] = a[l][l] + t * temp
    for i in range(k):
        temp = a[i][k]
        a[i][k] = temp - s * (a[i][l] + tau * temp)
        a[i][l] = a[i][l] + s * (temp - tau * a[i][l])
    for i in range(k + 1, l):
        temp = a[k][i]
        a[k][i] = temp - s * (a[i][l] + tau * a[k][i])
        a[i][l] = a[i][l] + s * (temp - tau * a[i][l])
    for i in range(l + 1, n):
        temp = a[k][i]
        a[k][i] = temp - s * (a[l][i] + tau * temp)
        a[l][i] = a[l][i] + s * (temp - tau * a[l][i])
    for i in range(n):
        temp = p[i][k]
        p[i][k] = temp - s * (p[i][l] + tau * p[i][k])
        p[i][l] = p[i][l] + s * (temp - tau * p[i][l])


def jacobi(a, tol=1.0e-9):
    n = len(a)
    max_rot = 5 * (n ** 2)
    p = []
    for i in range(0, n, 1):
        row = []
        for j in range(0, n, 1):
            if i == j:
                row.append(1)
            else:
                row.append(0)
        p.append(row)
    for i in range(max_rot):
        a_max, k, l = max_elem(a)
        if a_max < tol:
            diagonal = []
            for i in range(0, n, 1):
                for j in range(0, n, 1):
                    if i == j:
                        diagonal.append(a[i][j])
                    else:
                        continue
            return diagonal, p
        rotate(a, p, k, l)
    print('Jacobi method did not converge')
