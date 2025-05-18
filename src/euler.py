import numpy as np
from signal_generator import signal_generator


def sim_Euler(k, J, r, M, b, h, tmax, amp, freq, signal_type):

    A = np.array([[0, 1], [k / ((J / (r**2)) - M), -b / (r**2 * ((J / (r**2)) - M))]])
    B = np.array([[0], [-1 / ((J / (r**2)) - M)]])

    x0 = np.array([0, 0])  # Starting values
    steps = int(tmax / h)
    x = np.zeros((steps + 1, 2))
    x[0] = x0

    signal = signal_generator(signal_type, amp, freq, tmax, steps)
    print(signal)
    for n in range(steps):
        u_t = signal[n]
        x[n + 1] = x[n] + h * (np.dot(A, x[n]) + B.flatten() * u_t)

    interval = int(0.1 / h)
    for i in range(0, steps, interval):
        print(f"{i * h:.1f}  {x[i,0]:.3f}  {x[i,1]:.3f} {signal[i]:.3f}")

    # Dislay last value
    print(f"{(steps-1) * h:.1f}  {x[(steps-1),0]:.3f}  {x[(steps-1),1]:.3f}")

    return x
