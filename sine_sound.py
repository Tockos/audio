import math as m
import matplotlib.pyplot as plt
import numpy as np
import cmath
from bisect import bisect_right
import sounddevice as sd
from sine_wave import *

t_max = 3  # s
t_shift = 1  # s
f_sampling = 24000  # Hz
t_sampling = 1 / f_sampling  # s
N = t_max * f_sampling

t = np.array([k * t_sampling for k in range(N)])

f_base = 440
freqs = [f_base, f_base * 5 / 4, f_base * 3 / 2]
amps = [0.5, 0.4, 0.3]
shifts = [1, 2]  # sec

sine_waves = [SineWave(t_max=3, frequency=f, amplitude=amp) for f, amp in zip(freqs, amps)]
sine_waves[1].shift(shifts[0])
sine_waves[2].shift(shifts[1])

sound = np.sum(sine_waves)
# sd.play(sound.tone, f_sampling)
# status = sd.wait()  # Wait until file is done playing

num_of_periods = 10
point_num = num_of_periods * sine_waves[0].samples_in_period

from_idx = shifts[1]*sine_waves[0].fs
plt.plot(sound.tone[from_idx:from_idx+point_num])
plt.show()
