from algo.euler import *
from algo.rk import *
from matplotlib.pyplot import *
from math import sqrt

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

def main():
    T = 10  # end of simulation
    N = 20  # no of time steps
    time = np.linspace(0, T, N + 1)

    z0 = np.zeros(2)
    z0[0] = 2.0

    zrk4 = rk4(f, z0, time)  # compute response with constant CD using RK4
    ze = euler(f, z0, time)

    k1 = sqrt(g * 4 * rho_s * d / (3 * rho_f * CD))
    k2 = sqrt(3 * rho_f * g * CD / (4 * rho_s * d))
    v_a = k1 * np.tanh(k2 * time)  # compute response with constant CD using analytical solution

    legends = []
    line_type = ['-', ':', '.', '-.', ':', '.', '-.']
    plot(time, v_a, line_type[0])

    plot(time, ze[:, 1], line_type[1])
    legends.append('Euler(constantCD)')

    legends.append('RK4 (constant CD)')
    plot(time, zrk4[:, 1], line_type[3])

    legend(legends, loc='best', frameon=False)
    xlabel('Time [s]')
    ylabel('Velocity [m/s]')
    show()


if __name__ == '__main__':
    main()