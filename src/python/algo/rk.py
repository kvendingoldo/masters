import numpy as np
from matplotlib.pyplot import *

g = 9.81  # Gravity m/s^2
d = 41.0e-3  # Diameter of the sphere
rho_f = 1.22  # Density of fluid [kg/m^3]
rho_s = 1275  # Density of sphere [kg/m^3]
nu = 1.5e-5  # Kinematical viscosity [m^2/s]
CD = 0.4  # Constant drag coefficient


def f(z, t):
    """2x2 system for sphere with constant drag."""
    zout = np.zeros_like(z)
    alpha = 3.0 * rho_f / (4.0 * rho_s * d) * CD
    zout[:] = [z[1], g - alpha * z[1] ** 2]
    return zout


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

        print(func(z[i, :], t))

        k1 = np.asarray(func(z[i, :], t))  # predictor step 1
        k2 = np.asarray(func(z[i, :] + k1 * dt2, t + dt2))  # predictor step 2
        k3 = np.asarray(func(z[i, :] + k2 * dt2, t + dt2))  # predictor step 3
        k4 = np.asarray(func(z[i, :] + k3 * dt, t + dt))  # predictor step 4
        z[i + 1, :] = z[i, :] + dt / 6.0 * (k1 + 2.0 * k2 + 2.0 * k3 + k4)  # Corrector step
    return z


# main program starts here
T = 10  # end of simulation
N = 20  # no of time steps
time = np.linspace(0, T, N + 1)

z0 = np.zeros(2)
z0[0] = 2.0

zrk4 = rk4(f, z0, time)  # compute response with constant CD using RK4
k1 = np.sqrt(g * 4 * rho_s * d / (3 * rho_f * CD))
k2 = np.sqrt(3 * rho_f * g * CD / (4 * rho_s * d))
v_a = k1 * np.tanh(k2 * time)  # compute response with constant CD using analytical solution


legends=[]
line_type=['-',':','.','-.',':','.','-.']
plot(time, v_a, line_type[0])

print(zrk4)


legends.append('RK4 (constant CD)')
plot(time, zrk4[:,1], line_type[3])

legend(legends, loc='best', frameon=False)
xlabel('Time [s]')
ylabel('Velocity [m/s]')
#show()
#savefig