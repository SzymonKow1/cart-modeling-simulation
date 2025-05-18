from euler import sim_Euler
from rk4 import sim_rk4
from tkinter import *
from tkinter import messagebox

# default values
k = 10
J = 0.5
r = 2
M = 1
b = 0.1

h = 0.0001 # discretization time constant
tmax = 10
u_t = 1 # input signal


root = Tk()
root.title("cart-modeling-simulation")

Label(root, text='Enter sim values:').grid(row=0, sticky=W, padx=10, pady=5)

Label(root, text='Const k').grid(row=1, sticky=W, padx=10, pady=5)
Label(root, text='Const J').grid(row=2, sticky=W, padx=10, pady=5)
Label(root, text='Const r').grid(row=3, sticky=W, padx=10, pady=5)
Label(root, text='Const M').grid(row=4, sticky=W, padx=10, pady=5)
Label(root, text='Const b').grid(row=5, sticky=W, padx=10, pady=5)

Label(root, text='Euler method specific values:').grid(row=6, sticky=W, padx=10, pady=5)
Label(root, text='Discretization time const').grid(row=7, sticky=W, padx=10, pady=5)
Label(root, text='Simulation time').grid(row=8, sticky=W, padx=10, pady=5)

Label(root, text='Runge-Kutta method specific values:').grid(row=9, sticky=W, padx=10, pady=5)
# TODO: Insert here Runge-Kutta values

Label(root, text='Pick method:').grid(row=10, sticky=W, padx=10, pady=5)

k_var = StringVar(value=str(k))
J_var = StringVar(value=str(J))
r_var = StringVar(value=str(r))
M_var = StringVar(value=str(M))
b_var = StringVar(value=str(b))
h_var = StringVar(value="{:.4f}".format(h))
tmax_var = StringVar(value=str(tmax))

e_k = Entry(root, textvariable=k_var)
e_J = Entry(root, textvariable=J_var)
e_r = Entry(root, textvariable=r_var)
e_M = Entry(root, textvariable=M_var)
e_b = Entry(root, textvariable=b_var)
e_h = Entry(root, textvariable=h_var)
e_tmax = Entry(root, textvariable=tmax_var)

e_k.grid(row=1, column=1, padx=10, pady=5)
e_J.grid(row=2, column=1, padx=10, pady=5)
e_r.grid(row=3, column=1, padx=10, pady=5)
e_M.grid(row=4, column=1, padx=10, pady=5)
e_b.grid(row=5, column=1, padx=10, pady=5)
e_h.grid(row=7, column=1, padx=10, pady=5)
e_tmax.grid(row=8, column=1, padx=10, pady=5)

method = IntVar(value=0)
euler_radio = Radiobutton(root, text="Euler", variable=method, value=0).grid(row=11, column=0, sticky=W, padx=10, pady=5)
rk_radio = Radiobutton(root, text="Runge-Kutta", variable=method, value=1).grid(row=11, column=1, sticky=W, padx=10, pady=5)

def start_sim():
    try:
        k = float(e_k.get())
        J = float(e_J.get())
        r = float(e_r.get())
        M = float(e_M.get())
        b = float(e_b.get())
        h = float(e_h.get())
        tmax = float(e_tmax.get())
        
        if method.get() == 0:
            sim_Euler(k, J, r, M, b, h, tmax, u_t)
        else:
            sim_rk4(k, J, r, M, b, h, tmax, u_t)
            pass           
    except ValueError:
        messagebox.showerror("Error", "invalid input")

start_button = Button(root, text="Start", command=start_sim, width=10)
start_button.grid(row=12, column=0, columnspan=2, pady=10)

root.mainloop()


