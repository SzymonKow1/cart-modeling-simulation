import numpy as np


def sim_Euler(A, B, h, steps, input_signal):

    x0 = np.array([0, 0])
    x = np.zeros((steps, 2))
    x[0] = x0


    for n in range(steps - 1):
        x[n + 1] = x[n] + h * (np.dot(A, x[n]) + B.flatten() * input_signal[n])

    x_e = x[:, 0]
    v_e = x[:, 1]
    return x_e, v_e
