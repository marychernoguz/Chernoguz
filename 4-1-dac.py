import RPi.GPIO as GPIO
dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

def decimal2binary(value):
    return [int(i) for i in bin(value)[2:].zfill(8)]

try:
    n = []
    f = True
    while (f):
        print ('введите число от 0 до 255')
        a = input()
        if (a == 'q'):
            f = False
            print ('unable value') 
            break
        if (int(a) < 0 or int(a) > 256):
            f = False
            print ('unable value')
            break

        n = decimal2binary(int(a))
        print (n)
        for i in range(8):
            GPIO.output(dac[i], n[i]) 
        print('предполагаемое значение напряжения', 3.3 / 256 * int(a), 'Вольт')  
         
except (KeyboardInterrupt):
     print ('unable value') 
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()    