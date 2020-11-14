
import numpy as np
from scipy.io.wavfile import write


_char_div = '0'
_letter_div = '0' * 3
_word_div = '0' * 7

_letters = {
    'a': '13',
    'b': '3111',
    'c': '3131',
    'd': '311',
    'e': '1',
    'f': '1131',
    'g': '331',
    'h': '1111',
    'i': '11',
    'j': '1333',
    'k': '313',
    'l': '1311',
    'm': '33',
    'n': '31',
    'o': '333',
    'p': '1331',
    'q': '3313',
    'r': '131',
    's': '111',
    't': '3',
    'u': '113',
    'v': '1113',
    'w': '133',
    'x': '3113',
    'y': '3133',
    'z': '3311',
    '1': '13333',
    '2': '11333',
    '3': '11133',
    '4': '11113',
    '5': '11111',
    '6': '31111',
    '7': '33111',
    '8': '33311',
    '9': '33331',
    '0': '33333',
}

def encode(msg):
    """
    Encode msg with the international morse alphabeth and return with binary str
    """

    msg = msg.lower()

    invalid = list(set(msg) - set(_letters) - {' '})
    if invalid:
        raise ValueError(f"Invalid characters: {invalid}")

    words = []
    for word in msg.split(' '):

        letters = []
        for code in map(lambda k: _letters[k], word):

            letter = ['1' * int(length) for length in code]
            letters.append(_char_div.join(letter))

        words.append(_letter_div.join(letters))
    return _word_div.join(words)


def modulate(binary, freq=440, fs=24000):
    """
    Create amplitude modulated sine wave based on the binary str morse code
    """

    bits = len(binary)
    samples = bits * fs
    time = np.linspace(0, bits, samples)

    carrier = np.sin(2*np.pi * freq * time)

    unit = int(samples / bits)
    for i, bit in enumerate(binary):
        s = slice(i * unit, (i+1) * unit)
        carrier[s] *= int(bit)

    return carrier


def save(path, wave, fs=24000):
    write(path, fs, wave)


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import sounddevice as sd

    encoded = encode('sos')
    print(encoded)

    sound = modulate(encoded)
    plt.plot(sound)
    plt.show()

    #sd.play(sound)
    #sd.wait()

    # save('alma.wav', sound)
