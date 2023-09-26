import RPi.GPIO as GPIO
import time

dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

def decimal2binary(value):
    return [int(i) for i in bin(value)[2:].zfill(8)]

try:
    print ('period')
    t = float(input())
    print ('kolichestvo')
    k = int(input())
    i = 0
    for _ in range (k):
        while i < 255:
            n = decimal2binary(i)
            GPIO.output(dac, n)
            i += 1
            print(3.3 / 256 * int(i))
            time.sleep(t/512) 

        while i > 0:
            n = decimal2binary(i)
            GPIO.output(dac, n)
            i -= 1
            print(3.3 / 256 * int(i))  
            time.sleep(t/512)       
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()    