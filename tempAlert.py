from machine import Pin, PWM
import time, sys, neopixel
from sht3x import SHT3X


np = neopixel.NeoPixel(Pin(5), 3)
led = Pin(19, Pin.OUT)
sht = Pin(21)
buzpin = Pin(18,Pin.OUT)
buzzer = PWM(buzpin)
buzzer.deinit()
sht30 = SHT3X()
tempvalue =30


def offrgb():
    np[0]=(0,0,0)
    np.write()
    print('off')
    
def onrgb():
    np[0]=(255,0,0)
    np.write()
    print('on')

def sht30sensor():
    while True:       
        temp,humi=sht30.getTempAndHumi()
        print('temp :',temp,'humidity :',humi)
        time.sleep_ms(1000)
        if temp >tempvalue:
            print('temp :',temp,'humidity :',humi)
            onrgb()
            alert()
            led(0)
            buzzer.duty(0)
            print('Heat detected')
        else:
            offrgb()
            led.on()

    
def buzz (buzz_freq, on_time, off_time):
    buzzer.init()
    buzzer.freq(buzz_freq)
    #onrgb(np)
    time.sleep_ms(on_time)
    buzzer.duty(0)
    #offrgb(np)
    time.sleep_ms(off_time)

def alert():
    for note in range(0,3):
        buzzer.duty(50)
        buzz (1760, 500, 200)
    buzzer.duty(0)
    buzzer.deinit()



try:
    #sht.irq(trigger=3, handler=sht30sensor)
    sht30sensor()
except KeyboardInterrupt:
    buzzer.duty(0)
    offrgb()
    print('End')
    sys.exit(0)
