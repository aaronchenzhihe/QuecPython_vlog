#EC600U
from misc import ADC
from machine import Pin
import _thread
import utime
from misc import PWM_V2

def fun():
    while True:
        num=adc.read(adc.ADC0)
        utime.sleep(1)#出现具体电压值，通过电压值控制占空比
        return num

def LED_SW(num):
    if num<250:
        LED.write(0)
        print("led off")
    else:
        LED.write(1)
        print("led on")
        
if __name__=='__main__':
    LED=Pin(22,Pin.OUT,Pin.PULL_DISABLE,0)
    adc = ADC()
    adc.open()
    _thread.start_new_thread(fun,())
    while True:
        num=fun()        
        LED_SW(num)
