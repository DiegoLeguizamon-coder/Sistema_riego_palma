from machine import Pin as pin
from utime import sleep, sleep_ms
# Modulo del sensor dht
from dht import DHT11

sensor = DHT11(pin(15))

def start_sensor():
    retry = 0
    while retry < 3:
        try:
            sensor.measure()
            break
        except:
            retry = retry + 1
            print(".", end = "")
               
def temperature():
    start_sensor()
    return (sensor.temperature())

def humidity():
    start_sensor()
    return (sensor.humidity())