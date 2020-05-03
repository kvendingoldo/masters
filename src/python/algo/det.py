# -*- coding: utf-8 -*-
# @Author: Alexander Sharov

import copy


def determinant_recursive(A, total=0):
    indices = list(range(len(A)))

    if len(A) == 2 and len(A[0]) == 2:
        val = A[0][0] * A[1][1] - A[1][0] * A[0][1]
        return val

    for fc in indices:
        As = copy.deepcopy(A)
        As = As[1:]
        height = len(As)

        for i in range(height):
            As[i] = As[i][0:fc] + As[i][fc + 1:]

        sign = (-1) ** (fc % 2)
        sub_det = determinant_recursive(As)

        total += sign * A[0][fc] * sub_det

    return total
