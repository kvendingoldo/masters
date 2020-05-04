import numpy as np


def rk4(func, z0, time):
    """The Runge-Kutta 4 scheme for solution of systems of ODEs.
    z0 is a vector for the initial conditions,
    the right hand side of the system is represented by func which returns
    a vector with the same size as z0 ."""
    z = np.zeros((np.size(time), np.size(z0)))
    z[0, :] = z0
    zp = np.zeros_like(z0)
    for i, t in enumerate(time[0:-1]):
        dt = time[i + 1] - time[i]
        dt2 = dt / 2.0

        k1 = func(z[i, :], t)  # predictor step 1
        k2 = func(z[i, :] + k1 * dt2, t + dt2)  # predictor step 2
        k3 = func(z[i, :] + k2 * dt2, t + dt2)  # predictor step 3
        k4 = func(z[i, :] + k3 * dt, t + dt)  # predictor step 4
        z[i + 1, :] = z[i, :] + dt / 6.0 * (k1 + 2.0 * k2 + 2.0 * k3 + k4)  # Corrector step
    return z
