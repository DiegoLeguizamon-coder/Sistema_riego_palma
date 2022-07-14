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
    print("Conexión exitosa!")
    print('Datos de la red (IP/netmask/gw/DNS):', miRed.ifconfig())

#firebase example
import ufirebase as firebase
firebase.setURL("https://curso-android-firebase-6ae58-default-rtdb.firebaseio.com/")

def enviar_datos():
    for i in range(5):
        temp = random.randint(0, 100)
        hum = random.randint(0, 100)
        luz = random.randint(0, 100)
        firebase.addto("project2/palma2", {"temp": temp, "humedad": hum, "luz": luz},  bg=0)
        
enviar_datos()
print("Envio OK")