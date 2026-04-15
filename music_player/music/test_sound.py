import wave
import struct
import math

file = wave.open('test.wav', 'w')
file.setnchannels(1)
file.setsampwidth(2)
file.setframerate(44100)

duration = 2  # секунд
frequency = 440  # звук

for i in range(44100 * duration):
    value = int(32767.0 * math.sin(2 * math.pi * frequency * i / 44100))
    data = struct.pack('<h', value)
    file.writeframesraw(data)

file.close()