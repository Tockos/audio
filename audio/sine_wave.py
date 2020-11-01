import numpy as np
from audio.wave import Wave


class SineWave(Wave):
    def __init__(self, t_max=1, fs=24000, f=440, amp=1, phase=0):
        self._f = f
        self._amp = amp
        self._phase = phase
        self._t_max = t_max

        super(SineWave, self).__init__([], fs)
        self._calculate()

    def _calculate(self):
        """
        Calculate the elements of ndarray based on the values
        """
        t = np.array([k / self.fs for k in range(np.round(self.t_max * self.fs))])
        self._data  = self.amp * np.cos(2 * np.pi * self.f * t + self.phase)

    @property
    def f(self):
        return self._f

    @f.setter
    def f(self, value):
        self._f = value
        self._calculate()

    @property
    def amp(self):
        return self._amp

    @amp.setter
    def amp(self, value):
        self._amp = value
        self._calculate()

    @property
    def phase(self):
        return self._phase

    @phase.setter
    def phase(self, value):
        self._phase = value
        self._calculate()

    @property
    def t_max(self):
        return self._t_max

    @t_max.setter
    def t_max(self, value):
        self._t_max = value
        self._calculate()

    @property
    def period_len(self):
        return int(self.fs / self.f)

    def slice(self, start=0, end=None, unit='period'):
        """
        Return slice of the wave

        :param start: index of starting point (default: 0)
        :param end: index of end point (default: end of the array)
        :param unit: 'period' or 'point'
        :returns: SineWave object
        """

        if unit not in ['period', 'point']:
            raise ValueError("Invalid unit '%s'" % unit)

        # Calculate start and end index
        if unit == 'period':
            start *= self.period_len
            end = end * self.period_len if end else len(self) -1
        else:
            end = end or len(self) - 1

        if start < 0 or start > end or end > len(self):
            raise ValueError("Invalid index (start=%s, end=%s)" % (start, end))

        # TODO: Should return with SineWave object not ndarray!!!
        return self.data[int(start):int(end)]

