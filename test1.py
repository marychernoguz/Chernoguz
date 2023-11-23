import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
comp = 14

troyka= 13
GPIO.setup(troyka,GPIO.OUT,initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)
def decimal2binary (value):
     return [int(element) for element in bin(value)[2:].zfill(8)]
  
def adc ():
    itog = 0
    perem = 0  
    for i in range(8,1,-1):
            p2 = 2**i
            perem = itog + p2
            time.sleep(0.05)
            comparatorval=GPIO.input(comp)
            if comparatorval == 0:
             itog = perem
    return itog
try:
    while 1:
     value=adc()   
     voltage=3.3/2**8*value
     print("value=",value)
     
finally:
   GPIO.output(troyka, 0)
   GPIO.cleanup() 