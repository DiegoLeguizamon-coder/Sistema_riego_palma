from machine import Pin, Timer
from utime import sleep
import network, time, urequests
import ujson

water_flow = Pin(23, Pin.IN)

np = 0 
url = "https://api.thingspeak.com/update?api_key=OVCEZPSQVOMLSKKG"

factorK = 7.5
pulseCouter = 0
reloj = Timer(0)

def conteo(pin):
    global np
    np += 1

def freq(timer):
    global np, Q
    frec = np     
    Q = frec / 7.5
    
    print(f"Value : {water_flow.value()}")
    print (f"f= {frec} y Q= {Q}")
    response = urequests.get(url+"&field5="+str(Q))
    print(f"Response TS: {response.status_code , response.text}")
    np = 0 

        
water_flow.irq(trigger = Pin.IRQ_RISING, handler = conteo)
reloj.init(mode= Timer.PERIODIC, period= 5000, callback= freq)