import numpy as np


def sim_rk4(A, B, k, J, r, M, b, h, steps, input_signal):

    x0 = np.array([0, 0])
    x = np.zeros((steps, 2))
    x[0] = x0

    for n in range(steps - 1):
        k1 = np.dot(A, x[n]) + B.flatten() * input_signal[n]
        k2 = np.dot(A, x[n] + 0.5 * h * k1) + B.flatten() * input_signal[n]
        k3 = np.dot(A, x[n] + 0.5 * h * k2) + B.flatten() * input_signal[n]
        k4 = np.dot(A, x[n] + h * k3) + B.flatten() * input_signal[n]
        x[n+1] = x[n] + (h/6)*(k1 + 2 * k2 + 2 * k3 + k4)

    x_rk4 = x[:, 0]
    v_rk4 = x[:, 1]
    return x_rk4, v_rk4