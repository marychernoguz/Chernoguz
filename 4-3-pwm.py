import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)

try:
    print('your persents')
    x = int(input())
    p = GPIO.PWM(24, 1000)
    p.start(x)
    input('press return stop:') 
    p.stop()
finally:
    GPIO.output(24, 0)
    GPIO.cleanup() 