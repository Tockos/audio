import numpy as np
import wave


class SineWave(wave.Wave):

    def __init__(self, t_max=1, fs=24000, frequency=440, amplitude=1, phase=0):
        self.f = frequency
        self.amp = amplitude
        self.phase = phase
        self.t_max = t_max
        sample_num = np.round(t_max * fs)
        self.ts = 1 / fs
        self.t = np.array([k * self.ts for k in range(sample_num)])
        tone = self.amp * np.cos(2 * np.pi * self.f * self.t + phase)
        super(SineWave, self).__init__(tone, fs)

    @property
    def samples_in_period(self):
        return int(self.fs / self.f)
