import winsound

def c(duration=500):
    winsound.Beep(523, duration)

def d(duration=500):
    winsound.Beep(587, duration)

def e(duration=500):    
    winsound.Beep(659, duration)

def f(duration=500):
    winsound.Beep(698, duration)

def g(duration=500):
    winsound.Beep(784, duration)

def a(duration=500):
    winsound.Beep(880, duration)

def b(duration=500):
    winsound.Beep(987, duration)



song = [e, d, c, d, e, e, e, d, d, d, e, g, g, e, d, c, d, e, e, e, d, d, e, d, c ]

for note in song:
  note(1000)
#Made key
# winsound.Beep(c(fre), 500)
#winsound.Beep(e(fre), 500)
#winsound.Beep(f(fre), 500)

#Play music with file
#winsound.PlaySound('copycat.wav',winsound.SND_FILENAME)