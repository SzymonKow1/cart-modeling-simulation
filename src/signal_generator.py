import numpy as np
from scipy import signal as sig


def signal_generator(signal_type, amplitude, frequency, duration, steps):

    t = np.linspace(0, duration, steps, endpoint=False)
    match signal_type:
        case "rectangular":
            signal = amplitude * np.sign(np.sin(2 * np.pi * frequency * t))
        case "triangular":
            signal = amplitude * sig.sawtooth(2 * np.pi * frequency * t)
        case "harmonic":
            signal = amplitude * np.sin(2 * np.pi * frequency * t)
        case _:
            signal = np.ones(steps)
    return signal
