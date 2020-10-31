import numpy as np
from bisect import bisect_right


class Wave:
    def __init__(self, data: np.ndarray, fs: float):
        self.tone = data
        self.fs = fs

    def normalize(self):
        norm = max(abs(self.tone))
        if norm > 1:
            self.tone = self.tone / norm

    def __add__(self, other):
        if self.fs != other.fs:
            raise ValueError("fs doesn't match")

        extend_num = len(self) - len(other)
        if extend_num > 0:
            other.tone = np.concatenate((other.tone, np.zeros(extend_num)))
        elif extend_num < 0:
            self.tone = np.concatenate((self.tone, np.zeros(np.abs(extend_num))))

        return Wave(self.tone + other.tone, self.fs)

    def __len__(self):
        return self.tone.size

    def shift(self, t_sec):
        step_num = t_sec * self.fs
        self.tone = np.concatenate((np.zeros(step_num), self.tone))

