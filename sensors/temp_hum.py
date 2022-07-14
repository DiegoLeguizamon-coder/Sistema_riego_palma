from machine import Pin as pin
from utime import sleep, sleep_ms
# Modulo del sensor dht
from dht import DHT11

sensor = DHT11(pin(15))

def mapear(valor_sensor, minimo_entrada, maximo_entrada, minimo_salida, maximo_salida):
  valor_mapeado = (valor_sensor - minimo_entrada) * (maximo_salida - minimo_salida) / (maximo_entrada - minimo_entrada) + minimo_salida
  return valor_mapeado

while True:
    '''retry = 0
    while retry < 3:
        try:
            
            break
        except:
            retry = retry + 1
            print(".", end = "")'''
    sensor.measure()
    temp = (sensor.temperature())
    hum = (sensor.humidity())
    print("**"*30)
    print(f"La temperatura es : {temp}")
    print(f"La humedad es : {hum}")
    
    sleep(1)