import soundfile as sf
import sounddevice as sd

sig, fs = sf.read('i2s.raw', channels=2, samplerate=16000,
                  format='RAW', subtype='PCM_16')
sd.play(sig, fs)
