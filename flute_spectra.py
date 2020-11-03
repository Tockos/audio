import wave
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt

orig_flute = wave.open("examples/flute.wav", "rb")
flute_params = orig_flute.getparams()
fs = orig_flute.getframerate()
frames = orig_flute.readframes(orig_flute.getnframes())
dt = np.int16
samples = np.frombuffer(frames, dt)
samples32 = samples.astype(np.float32)
max_amp = 2**15
norm_samples = samples32/max_amp

# sd.play(norm_samples, 2*fs)
# status = sd.wait()  # Wait until file is done playing
a = 10
flute_spect = np.fft.rfft(abs(norm_samples))
plt.plot(flute_spect)
# plt.plot(norm_samples[:100000])
plt.show()
