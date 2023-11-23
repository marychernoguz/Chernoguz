import RPi.GPIO as GPIO
import time
import waveFunctions as w

height = 40
w.opendoor()
data = []
start = time.time()
finish = start

try:
    while (finish - start) < 15:
        data.append(w.adc())
        finish = time.time()
finally:
    GPIO.cleanup()
    w.save(data, start, finish, height)      