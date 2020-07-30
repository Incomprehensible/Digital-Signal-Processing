#!/bash/python3
import numpy as np
import wave
import struct
import matplotlib.pyplot as plt


freq = 1000
noise = 50

n_samples = 48000

sampling_rate = 48000.0

amplitude = 16000

file = 'sine.wav'

sine_wave = [np.sin(2 * np.pi * freq * x/sampling_rate) for x in range(n_samples)]
sine_noise = [np.sin(2 * np.pi * noise * x/sampling_rate) for x in range(n_samples)]

sine_wave = np.array(sine_wave)
sine_noise = np.array(sine_noise)

combined = sine_wave + sine_noise

n_frames = n_samples * 2

comptype = 'NONE'
compname = 'not compressed'

plt.subplot(3,1,1)
plt.title("Original wave")
plt.subplots_adjust(hspace=.5)
plt.plot(sine_wave[:500])
plt.subplot(3,1,2)
plt.title("Noise")
plt.plot(sine_noise[:4000])
plt.subplot(3,1,3)
plt.title("Combined")
plt.plot(combined[:3000])
plt.show()

data_fft = np.fft.fft(combined)
freq = np.abs(data_fft[:len(data_fft)])

plt.plot(freq)
plt.title("FFT on combined wave")
plt.xlim(0, 3000)
plt.show()

