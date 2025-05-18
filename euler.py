import numpy as np
import matplotlib.pyplot as plt

# k = 10
# J = 0.5
# r = 2
# M = 1
# b = 0.1
def sim_Euler(k,J,r,M,b,h,tmax,u_t):

    A = np.array([
        [0, 1],
        [k / ((J / (r**2)) - M), -b / (r**2 * ((J / (r**2)) - M))]
    ])
    B = np.array([[0], [-1 / ((J / (r**2)) - M)]])

    x0 = np.array([0, 0]) # Starting values
    steps = int(tmax / h) + 1
    x = np.zeros((steps, 2))
    x[0] = x0


    for n in range(steps - 1):
        x[n + 1] = x[n] + h * (np.dot(A, x[n]) + B.flatten() * u_t)

    interval = int(0.1 / h)
    for i in range(0, steps, interval):
        print(f"{i * h:.1f}  {x[i,0]:.3f}  {x[i,1]:.3f}")
        
    # Display last value
    print(f"{(steps-1) * h:.1f}  {x[(steps-1),0]:.3f}  {x[(steps-1),1]:.3f}")

    return x

