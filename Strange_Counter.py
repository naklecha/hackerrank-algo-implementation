t = int(raw_input())

phase = 3
while t > phase:
    t -= phase
    phase *= 2

print phase - t + 1
