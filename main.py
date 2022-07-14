from machine import Pin as pin, ADC, PWM
from utime import sleep, sleep_ms
import network, time, urequests



#------------------------Conexión a wifi------------------------
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
    
    
#-----------------------Fin Conexión a Wifi--------------------------------

#----------------Función Mapeo-----------------------------------------

def mapear(valor_sensor, minimo_entrada, maximo_entrada, minimo_salida, maximo_salida):
  valor_mapeado = (valor_sensor - minimo_entrada) * (maximo_salida - minimo_salida) / (maximo_entrada - minimo_entrada) + minimo_salida
  return valor_mapeado

#---------------------Fin Mapeo---------------------------------------

#-------------------Servo ------------------------
servo=PWM(pin(14), freq=50)

def open():
    for i in range(18,136):
        servo.duty(i)
        #   servo.duty16(i) Mayor presición
        sleep(0.1)

def close():
    for i in range(136,18,-1):
        servo.duty(i)
        sleep(0.1)
        
#------------------- Fin Servo ------------------------

#--------------------Sensor Suelo ---------------------------
sensorACSuelo=ADC(pin(32))
sensorACSuelo.atten(ADC.ATTN_11DB)
#--------------------Fin Sensor Suelo ---------------------------


#--------------------Sensor Luz Ambiente ----------------------
sensorAC_1=ADC(pin(35))
sensorAC_1.atten(ADC.ATTN_11DB)
    
#--------------------Sensor Luz Ambiente ----------------------

#-----------------------Sensor Luz normal --------------------
sensorAC=ADC(pin(34))
sensorAC.atten(ADC.ATTN_11DB)
#-----------------------Fin Sensor Luz normal --------------------

#--------------------Sensor temp_hum-------------------
from dht import DHT11
sensor = DHT11(pin(15))
#--------------------Fin Sensor temp_hum-------------------

#----------------------Relay------------------------
relay = pin(4, pin.OUT)

#-------------------Firebase ------------------------------

#import ufirebase as firebase
#firebase.setURL("https://curso-android-firebase-6ae58-default-rtdb.firebaseio.com/")

#url = "https://api.thingspeak.com/update?api_key=LGCLNYYRP7WRBFEL"

#----------------------Lógica ---------------------

for i in range(100):
    '''
    #hum_suelo_D = sensor.value()
    hum_suelo_AC=sensorAC.read()
    #print(hum_suelo_AC)
    print("*"*32)
    print(f"Humedad de suelo: {hum_suelo_AC}")
    hum_suelo_AC=mapear(hum_suelo_AC,0,4095,100,0)
    sleep(1)
    print(f"Humedad de suelo: {hum_suelo_AC}%")
    print("*"*32) '''
    
    hum_suelo_AC=sensorACSuelo.read()
    #hum_suelo_AC=mapear(hum_suelo_AC,0,4095,100,0)
    luz_amb_AC=sensorAC.read()
    luz_AC=sensorAC_1.read()
    
    print("*"*32)
    print(f"Toma de datos: {i}")
    print(f"Humedad de suelo: {hum_suelo_AC}")
    print(f"Luz ambiente: {luz_amb_AC}")
    print(f"Luz normal: {luz_AC}")
    retry = 0
    while retry < 3:
        try:
            sensor.measure()
            temp = (sensor.temperature())
            hum = (sensor.humidity())
            break
        except:
            retry = retry + 1
            print(".", end = "")

    '''sensor.measure()
    temp = (sensor.temperature())
    hum = (sensor.humidity())'''
    print(f"La temperatura es : {temp}")
    print(f"La humedad es : {hum}")
    
    if hum>=65:
        relay.value(1)
        print(f"Estado Relay {relay.value()}")
    else:
        relay.value(0)
        print(f"Estado Relay {relay.value()}")
    
    #firebase.addto("project/palma", {"temperature": temp,"humidity":hum,"humidity_floor": hum_suelo_AC, "regular_light": luz_AC, "ambient_light": luz_amb_AC},  bg=0)
    #respuesta = urequests.get(url+"&field1="+str(temp)+"&field2="+str(hum)+"&field3="+str(hum_suelo_AC)+"&field4="+str(luz_AC)+"&field=5"+str(luz_amb_AC))
    
    if hum_suelo_AC>=3000:
        print("Humedad baja, abrir llave de riego")
        #open()
    else:
        print("Humedad alta, cerrar llave de riego")
        #close()
    print("*"*32)
    print(" ")
    sleep(2)
    
