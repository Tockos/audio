import numpy as np


class Wave:
    def __init__(self, data, fs=1):
        self._data = np.array(data)
        self.fs = fs
        self.ts = 1 / fs

    def __repr__(self):
        return "%s(%s)" % (self.__class__.__name__, self.data)

    def __len__(self):
        return len(self.data)

    def __eq__(self, other):
        if self.__class__ != other.__class__ or self.fs != other.fs:
            return False

        if len(self.data) == len(other.data) == 0:
            # Comparison of empty arrays return with False by default
            return True

        # The array comparison returns with a list of bools
        return all(self.data == other.data)

    @property
    def data(self):
        return self._data

    def extend(self, array, left=False):
        """
        Extend current array with another

        :param left: bool - extend on the left side. Other on the right side
        :param array: array - array to extend with
        :returns: extended copy object
        """

        data = (self._data, array)
        #data = (array, self._data) if left is True else (self._data, array)
        self._data =  np.concatenate(data)

    def norm(self, reference=1):
        """
        Normalize data with reference number

        :param reference: reference number for aligning the data to.
        """

        maximum = max(abs(self.data))
        if maximum > reference:
            self._data /= maximum

    def shift(self, t_sec):
        """
        Shift the data with t_sec by adding zeros to the array.

        :param t_sec: seconds to shift the data (right if > 0; left if < 0)
        :returns: right shifted copy object
        """

        self.extend(np.zeros(t_sec * self.fs), left=t_sec < 0)

    def __add__(self, other):
        if self.fs != other.fs:
            raise ValueError("fs doesn't match")

        # Extend the smaller array if there is diff
        diff = len(self) - len(other)
        if diff > 0:
            other.extend(np.zeros(diff))
        elif diff < 0:
            self.extend(np.zeros(abs(diff)))

        # Add element by element to avoid endless recursion
        return Wave(self.data + other.data, fs=self.fs)
