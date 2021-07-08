def play_data(filename, first_sec, second_sec):
  import ao
  from ao import AudioDevice 
  dev = AudioDevice(2, bits=16, rate=16000,channels=1)
  f = open(filename, 'r')
  data_len = (second_sec-first_sec)*32000
  f.seek(32000*first_sec)
  data = f.read(data_len)
  dev.play(data)
  f.close()

play_data('i2s.raw', 2.5, 5)
