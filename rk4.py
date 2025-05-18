import numpy as np
import matplotlib.pyplot as plt

def sim_rk4(k, J, r, M, b, h, tmax, u_t):
    A = np.array([
        [0, 1],
        [k / ((J / (r ** 2)) - M), -b / (r ** 2 * ((J / (r ** 2)) - M))]
    ])
    B = np.array([[0], [-1 / ((J / (r ** 2)) - M)]])

    x0 = np.array([0, 0])
    steps = int(tmax / h) + 1
    x = np.zeros((steps, 2))
    x[0] = x0

    for n in range(steps - 1):
        k1 = np.dot(A, x[n]) + B.flatten() * u_t
        k2 = np.dot(A, x[n] + 0.5 * h * k1) + B.flatten() * u_t
        k3 = np.dot(A, x[n] + 0.5 * h * k2) + B.flatten() * u_t
        k4 = np.dot(A, x[n] + h * k3) + B.flatten() * u_t
        x[n+1] = x[n] + (h/6)*(k1 + 2 * k2 + 2 * k3 + k4)

    interval = int(0.1 / h)

    for i in range(0, steps, interval):
        print(f"{i * h:.1f}  {x[i, 0]:.3f}  {x[i, 1]:.3f}")

    # Display last value
    print(f"{(steps - 1) * h:.1f}  {x[(steps - 1), 0]:.3f}  {x[(steps - 1), 1]:.3f}")

    t = np.linspace(0, tmax, steps)
    plt.plot(t, x[:, 0])
    plt.plot(t, x[:, 1])
    plt.grid(True)
    plt.show()

    return x