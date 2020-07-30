#!/bash/python3
import numpy as np
import wave
import struct
import matplotlib.pyplot as plt

frame_rate = 48000.0
input = 'sine.wav'
n_samples = 48000
wav_file = wave.open(input, 'r')
data = wav_file.readframes(n_samples)
wav_file.close()
data = struct.unpack('{n}h'.format(n=n_samples), data)
data = np.array(data)

# get the array of complex numbers with all the frequencies present in the signal wave
data_fft = np.fft.fft(data)

# convert complex numbers to real numbers; aka generate real part of the complex signal
frequencies = np.abs(data_fft)

print("The frequency spectrum is dominated by {hz} Hz".format(hz=np.argmax(frequencies)))

plt.subplot(2,1,1)
plt.plot(data[:300])
plt.title("Original wave")
plt.subplot(2,1,2)
plt.plot(frequencies)
plt.title("Frequencies found")
plt.xlim(0,3000)
plt.show()



