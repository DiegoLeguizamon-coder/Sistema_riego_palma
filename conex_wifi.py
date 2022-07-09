import network, time, urequests
from machine import Pin
import urequests
import ujson
from utime import sleep
import random

def conectaWifi(red, password):
     global miRed
     miRed = network.WLAN(network.STA_IF)     
     if not miRed.isconnected():              #Si no está conectado…
          miRed.active(True)                   #activa la interface
          miRed.connect(red, password)         #Intenta conectar con la red
          print('Conectando a la red', red +"…")
          timeout = time.time ()
          while not miRed.isconnected():           #Mientras no se conecte..
              if (time.ticks_diff (time.time (), timeout) > 10):
                  return False
     return True
    
if conectaWifi("Tech_001", "1019077632"):
    print("Conexión exitosa!!!!!!!!!!!!!!!!!!!")
    print('Datos de la red (IP/netmask/gw/DNS):', miRed.ifconfig())
