#!/bash/python3
import numpy as np
import wave
import struct
import matplotlib.pyplot as plt

# Sine wave formula
# y(x) = A * sin(2 * pi * f * t)
# y(t) is the y axis sample we want to calculate for x axis sample t.
# f - frequency - the n of times a wave repeats a sec
# A - amplitude
# t - out sample; divide by sampling rate (measures/sec) to convert to digital

# 2000 - 400 my fav
freq = 2000
freq2 = 400
# sampling rate of 48000 is used in professional environments
# audio in the form of wav files is made of 16-bit integer. thus full scale amplitude is 32767 (2^15 – 1)
# we multiply generated wave (floating point) by a fixed A value to get integer wave

n_samples = 48000

# The sampling rate of the analog to digital convert
sampling_rate = 48000.0

amplitude = 16000

file = 'sine.wav'

sine_wave = [np.sin(2 * np.pi * freq * x/sampling_rate) for x in range(n_samples)]
sine_wave2 = [np.sin(2 * np.pi * freq2 * x/sampling_rate) for x in range(n_samples)]

# n of frames or samples
n_frames = n_samples * 2

# compression
comptype = 'NONE'
compname = 'not compressed'

n_channels = 1

# sample width - 16 bits or 2 bytes
sampwidth = 2

wav_file = wave.open(file, 'w')
wav_file.setparams((n_channels, sampwidth, int(sampling_rate), n_frames, comptype, compname))

# for s in sine_wave:
# 	wav_file.writeframes(struct.pack('h', int(s * amplitude)))
# for s in sine_wave2:
# 	wav_file.writeframes(struct.pack('h', int(s * amplitude)))
achord = []
for z in zip(sine_wave, sine_wave2):
	achord.append(z[0])
	achord.append(z[1])
for s in achord:
	wav_file.writeframes(struct.pack('h', int(s * amplitude)))


