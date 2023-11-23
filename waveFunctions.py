import spidev  
import RPi.GPIO as GPIO
import time
import numpy as np
spi = spidev.SpiDev()
GPIO.setmode(GPIO.BCM)
comp = 14
troyka = 13
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]
bites = 8


dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)
def adc():
    value_res = 0
    temp_value = 0
    for i in range(bites):
        pow2 = 2 ** (bites - i - 1)
        temp_value = value_res + pow2
        signal = decimal2binary(temp_value)
        GPIO.output(dac, signal)
        time.sleep(0.005)
        compVal = GPIO.input(comp)
        if compVal == 0:
            value_res = temp_value
    return value_res

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN)

def opendoor():
    print(GPIO.input(21))
    time.sleep(0.5)
    return GPIO.input(21) 

def save (samples, start, finish, height):
    filename = 'data {}{} mm.txt'.format(time.strftime('S', time.localtime(start)), height)

    with open(filename, "w") as outfile:
        outfile.write (time.strftime('S', time.localtime(time.time())))
        outfile.write (str(finish - start))
        np.savetxt(outfile, np.array(samples).T, fmt = '%d')