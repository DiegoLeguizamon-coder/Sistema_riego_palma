from machine import Pin as pin, ADC, PWM
from utime import sleep, sleep_ms
import network, time, urequests

led = pin(2, pin.OUT)

def pruebaMetodo():
    while True:
        led.value(1)
        sleep(0.5)
        led.value(0)
        sleep(0.05)
        print("Hola de nuevo")