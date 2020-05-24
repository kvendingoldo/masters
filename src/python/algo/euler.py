# -*- coding: utf-8 -*-
# @Author: Alexander Sharov

import numpy as np


def euler(func, z0, time):
    """The Euler scheme for solution of systems of ODEs.
    z0 is a vector for the initial conditions,
    the right hand side of the system is represented by func which returns
    a vector with the same size as z0 ."""
    z = np.zeros((np.size(time), np.size(z0)))
    z[0, :] = z0
    for i in range(len(time) - 1):
        dt = time[i + 1] - time[i]
        z[i + 1, :] = z[i, :] + func(z[i, :], time[i]) * dt
    return z