import numpy as np
from audio.wave import Wave


class SineWave(Wave):

    def __new__(cls, t_max=1, fs=24000, f=440, amp=1, phase=0):
        sample_num = np.round(t_max * fs)
        t = np.array([n / fs for n in range(sample_num)])
        tone = amp * np.cos(2 * np.pi * f * t + phase)
        obj = super(SineWave, cls).__new__(cls, tone, fs)
        obj.f = f
        obj.amp = amp
        obj.phase = phase
        obj.t_max = t_max
        return obj


    @property
    def samples_in_period(self):
        return int(self.fs / self.f)
