import math as m
import matplotlib.pyplot as plt
import numpy as np
import cmath
from bisect import bisect_right
import sounddevice as sd
from audio.sine_wave import SineWave
from audio.wave import Wave

t_max = 3  # s
t_shift = 1  # s
f_sampling = 24000  # Hz
t_sampling = 1 / f_sampling  # s
N = t_max * f_sampling

t = np.array([k * t_sampling for k in range(N)])

f_base = 440
freqs = [f_base, f_base * 5 / 4, f_base * 3 / 2]
amps = [0.5, 0.3, 0.2]
shifts = [1, 2]  # sec

sine_waves = [SineWave(t_max=3, f=f, amp=amp) for f, amp in zip(freqs, amps)]
# sine_waves[1].shift(shifts[0])
# sine_waves[2].shift(shifts[1])

example = np.add(sine_waves[0], sine_waves[1])
sound = np.sum(sine_waves)
sound.norm()
# sd.play(sound.tone, f_sampling)
# status = sd.wait()  # Wait until file is done playing

num_of_periods = 3
point_num = num_of_periods * sine_waves[0].samples_in_period

from_idx = shifts[1]*sine_waves[0].fs
fig, subplots = plt.subplots(2)

subplots[0].plot(sound.t_space[from_idx:from_idx+point_num], sound.tone[from_idx:from_idx+point_num])

N = len(sound.tone)
spect = np.fft.fftshift(np.fft.fft(sound.tone))
freq_space = np.linspace(-sine_waves[0].fs/2, sine_waves[0].fs/2, N)

r_spect = 2/N*np.fft.rfft(sound.tone)
r_freq_space = np.linspace(0, sine_waves[0].fs/2, int(np.ceil(N/2))+1)

# plt.plot(freq_space, np.abs(spect))
subplots[1].plot(r_freq_space, np.abs(r_spect))
# plt.plot(freq_space, np.arctan(spect.imag/spect.real))

plt.show()
