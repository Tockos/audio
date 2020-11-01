import numpy as np


class Wave(np.ndarray):
    def __new__(cls, array, fs=1):
        obj = np.asarray(array).view(cls)
        obj.fs = fs
        obj.ts = 1 / fs
        return obj

    @property
    def t_domain(self):
        return self.ts * np.array(range(len(self)))

    def __repr__(self):
        return "%s(%s)" % (self.__class__.__name__, self)

    def extend(self, array, left=False):
        """
        Extend current array with another

        :param left: bool - extend on the left side. Other on the rigth side
        :returns: extended copy object
        """

        data = (array, self) if left is True else (self, array)
        return np.concatenate(data).view(self.__class__)

    def norm(self, reference=1):
        """
        Normalize data with reference number

        :param reference: reference number for aligning the data to.
        """

        maximum = max(abs(self))
        if maximum > reference:
            self /= maximum

    def shift(self, t_sec):
        """
        Shift the data with t_sec by adding zeros to the array.

        :param t_sec: seconds to shift the data (right if > 0; left if < 0)
        :returns: right shifted copy object
        """

        return self.extend(np.zeros(t_sec * self.fs), left=t_sec < 0)

    def __add__(self, other):
        if self.fs != other.fs:
            raise ValueError("fs doesn't match")

        # Copy self object
        this = self

        # Extend the smaller array if there is diff
        diff = len(this) - len(other)
        if diff > 0:
            other = other.extend(np.zeros(diff))
        elif diff < 0:
            this = self.extend(np.zeros(abs(diff)))

        # Add element by element to avoid endless recursion
        return np.array([a + b for a, b in zip(this, other)]).view(Wave)
