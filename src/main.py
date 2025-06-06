from euler import sim_Euler
from rk4 import sim_rk4
from signal_generator import signal_generator


from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np

# default values
k = 10
J = 0.5
r = 2
M = 1
b = 0.1

h = 0.001
tmax = 10

amplitude = 1
frequency = 1


root = Tk()
root.title("cart-modeling-simulation")

Label(root, text="Enter sim values:").grid(row=0, sticky=W, padx=10, pady=5)

Label(root, text="Const k").grid(row=1, sticky=W, padx=10, pady=5)
Label(root, text="Const J").grid(row=2, sticky=W, padx=10, pady=5)
Label(root, text="Const r").grid(row=3, sticky=W, padx=10, pady=5)
Label(root, text="Const M").grid(row=4, sticky=W, padx=10, pady=5)
Label(root, text="Const b").grid(row=5, sticky=W, padx=10, pady=5)

Label(root, text="Discretization time const").grid(row=7, sticky=W, padx=10, pady=5)
Label(root, text="Simulation time").grid(row=8, sticky=W, padx=10, pady=5)

Label(root, text="Input parameters:").grid(row=12, sticky=W, padx=10, pady=5)
Label(root, text="Amplitude").grid(row=13, sticky=W, padx=10, pady=5)
Label(root, text="Frequency (Hz)").grid(row=14, sticky=W, padx=10, pady=5)


Label(root, text="Signal type:").grid(row=15, sticky=W, padx=10, pady=5)


k_var = StringVar(value=str(k))
J_var = StringVar(value=str(J))
r_var = StringVar(value=str(r))
M_var = StringVar(value=str(M))
b_var = StringVar(value=str(b))
h_var = StringVar(value="{:.3f}".format(h))
tmax_var = StringVar(value=str(tmax))
amplitude_var = StringVar(value=str(amplitude))
frequency_var = StringVar(value=str(frequency))

e_k = Entry(root, textvariable=k_var)
e_J = Entry(root, textvariable=J_var)
e_r = Entry(root, textvariable=r_var)
e_M = Entry(root, textvariable=M_var)
e_b = Entry(root, textvariable=b_var)
e_h = Entry(root, textvariable=h_var)
e_tmax = Entry(root, textvariable=tmax_var)
e_amplitude = Entry(root, textvariable=amplitude_var)
e_frequency = Entry(root, textvariable=frequency_var)

e_k.grid(row=1, column=1, padx=10, pady=5)
e_J.grid(row=2, column=1, padx=10, pady=5)
e_r.grid(row=3, column=1, padx=10, pady=5)
e_M.grid(row=4, column=1, padx=10, pady=5)
e_b.grid(row=5, column=1, padx=10, pady=5)
e_h.grid(row=7, column=1, padx=10, pady=5)
e_tmax.grid(row=8, column=1, padx=10, pady=5)
e_amplitude.grid(row=13, column=1, padx=10, pady=5)
e_frequency.grid(row=14, column=1, padx=10, pady=5)


signal = StringVar(value="rectangular")
rectangular_radio = Radiobutton(
    root, text="rectangular", variable=signal, value="rectangular"
).grid(row=16, column=0, sticky=W, padx=10, pady=5)
triangular_radio = Radiobutton(
    root, text="triangular", variable=signal, value="triangular"
).grid(row=16, column=1, sticky=W, padx=10, pady=5)
harmonic_radio = Radiobutton(
    root, text="harmonic", variable=signal, value="harmonic"
).grid(row=16, column=2, sticky=W, padx=10, pady=5)


def start_sim():
    try:
        k = float(e_k.get())
        J = float(e_J.get())
        r = float(e_r.get())
        M = float(e_M.get())
        b = float(e_b.get())
        h = float(e_h.get())
        tmax = float(e_tmax.get())
        amp = float(e_amplitude.get())
        freq = float(e_frequency.get())
        signal_type = str(signal.get())

        A = np.array([
            [0, 1],
            [k / ((J / (r ** 2)) - M), -b / (r ** 2 * ((J / (r ** 2)) - M))]
        ])
        B = np.array([
            [0],
            [-1 / ((J / (r ** 2)) - M)]
        ])

        steps = int(tmax / h) + 1
        input_signal = signal_generator(signal_type, amp, freq, tmax, steps)

        [e_x, e_v] = sim_Euler(A, B, h, steps, input_signal)
        [rk4_x, rk4_v] = sim_rk4(A, B, h, steps, input_signal)


        plt.figure(figsize=(9, 16))
        t = np.linspace(0, tmax, steps)

        plt.subplot(3, 1, 1)
        plt.plot(t, input_signal, label="input", color="green")
        plt.grid(which='both', linestyle='--', linewidth=0.5)
        plt.minorticks_on()
        plt.grid(which='minor', linestyle=':', linewidth=0.5, alpha=0.5)
        plt.title("Input Signal vs. Time", fontsize=16, fontweight='bold')
        plt.xlabel("Time [s]")
        plt.ylabel("Amplitude")
        plt.legend()

        plt.subplot(3, 1, 2)
        plt.plot(t, e_x, label="Euler", color="red")
        plt.plot(t, rk4_x, label="rk4", color="blue")
        plt.grid(which='both', linestyle='--', linewidth=0.5)
        plt.minorticks_on()
        plt.grid(which='minor', linestyle=':', linewidth=0.5, alpha=0.5)
        plt.title("Position vs. Time", fontsize=16, fontweight='bold')
        plt.xlabel("Time [s]")
        plt.ylabel("Amplitude")
        plt.legend()

        plt.subplot(3, 1, 3)
        plt.plot(t, e_v, label="Euler", color="red")
        plt.plot(t, rk4_v, label="rk4", color="blue")
        plt.grid(which='both', linestyle='--', linewidth=0.5)
        plt.minorticks_on()
        plt.grid(which='minor', linestyle=':', linewidth=0.5, alpha=0.5)
        plt.title("Velocity vs. Time", fontsize=16, fontweight='bold')
        plt.xlabel("Time [s]")
        plt.ylabel("Amplitude")
        plt.legend()

        plt.tight_layout()
        plt.show()

    except ValueError as e:
        messagebox.showerror("Error", e)


start_button = Button(root, text="Start", command=start_sim, width=10)
start_button.grid(row=17, column=0, columnspan=2, pady=10)

root.mainloop()
