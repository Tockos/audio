#!/usr/bin/python3.7

from math import *
import matplotlib.pyplot as plt


class Function:
    def __init__(self, value):
        self._value = value


class Constant(Function):
    def __call__(self, it):
        return (self._value for _ in it)


class Linear(Function):
    def __call__(self, it):
        return (x + self._value for x in it)


class Parabole(Function):
    def __call__(self, it):
        return (x ** self._value for x in it)


class Exponent(Function):
    def __call__(self, it):
        return (self._value ** x for x in it)


class Logarithm:
    def __init__(self, base=e):
        self._base = base

    def __call__(self, it):
        return (log(x, self._base) for x in it)


class Sine:
    def __init__(self, amp=1, phase=0):
        self._amp = amp
        self._phase = phase

    def __call__(self, it):
        for x in it:
            yield self._amp * sin(x + self._phase)


def example_plot_parabole_sine():
    parabola = Parabole(2)
    sine = Sine()

    x = range(-1000, 1001)
    p = list(parabola(x))
    s = list(sine(x * 2 * pi / max(p) * 15 for x in p))

    fig, sub = plt.subplots(2)
    sub[0].plot(x, p)
    sub[1].plot(x, s)

    plt.show()


def example_plot_log_sine():
    """
    when phase is ln(x) freq is 1/x
    """

    logarithm = Logarithm()
    sine = Sine()

    x = range(1, 1000)
    l = list(logarithm(x))
    s = list(sine(x * 2 * pi / max(l) * 15 for x in l))

    fig, sub = plt.subplots(2)
    sub[0].plot(x, l)
    sub[1].plot(x, s)

    plt.show()


if __name__ == "__main__":
    example_plot_parabole_sine()
    # example_plot_log_sine()
