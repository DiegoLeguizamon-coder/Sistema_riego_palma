from machine import Pin as pin, ADC, PWM
from utime import sleep, sleep_ms, time
import network, time, urequests
import ujson
import random
from modules.WiFi_connection import connectWifi
from sensors.FC28_floor_humidity import floor_humidity
from sensors.DTH11_temperature_humidity import temperature, humidity
from sensors.LM193_ambient_light import ambient_light
import actuators.relay_ventilator as relay_ven

def mapear(valor_sensor, minimo_entrada, maximo_entrada, minimo_salida, maximo_salida):
  valor_mapeado = (valor_sensor - minimo_entrada) * (maximo_salida - minimo_salida) / (maximo_entrada - minimo_entrada) + minimo_salida
  return valor_mapeado

def sensor_data():
    global s_f_humidity
    global s_humidity
    global s_temperature
    global s_light
    s_f_humidity = floor_humidity()
    s_humidity = humidity()
    s_temperature = temperature()
    s_light = ambient_light()

if not connectWifi("Tech_001", "1019077632"):
    print("Error al conectar a la red.")
else:
    print("Conexión exitosa.")
    
while True:
    sensor_data()
    print("%"*32)
    print(f"Humedad de suelo: {s_f_humidity}%")
    print(f"Humedad: {s_humidity}%")
    print(f"Temperatura: {s_temperature}C")
    print(f"Luz ambiente: {s_light}%")
    print("%"*32)
    sleep(15)
    if relay_ven.validate_ventilator()== 1 :
        relay_ven.state_ventilator(0)
    else: 
        relay_ven.state_ventilator(1)
    

# #-------------------Firebase ------------------------------

# import modules.ufirebase as firebase
# firebase.setURL("https://curso-android-firebase-6ae58-default-rtdb.firebaseio.com/")

# #url = "https://api.thingspeak.com/update?api_key=LGCLNYYRP7WRBFEL"

# #----------------------Lógica ---------------------

# for i in range(100):
#     '''
#     #hum_suelo_D = sensor.value()
#     hum_suelo_AC=sensorAC.read()
#     #print(hum_suelo_AC)
#     print("*"*32)
#     print(f"Humedad de suelo: {hum_suelo_AC}")
#     hum_suelo_AC=mapear(hum_suelo_AC,0,4095,100,0)
#     sleep(1)
#     print(f"Humedad de suelo: {hum_suelo_AC}%")
#     print("*"*32) '''
    
#     hum_suelo_AC=sensorACSuelo.read()
#     #hum_suelo_AC=mapear(hum_suelo_AC,0,4095,100,0)
#     luz_amb_AC=sensorAC.read()
#     luz_AC=sensorAC_1.read()
    
#     print("*"*32)
#     print(f"Toma de datos: {i}")
#     print(f"Humedad de suelo: {hum_suelo_AC}")
#     print(f"Luz ambiente: {luz_amb_AC}")
#     print(f"Luz normal: {luz_AC}")
#     retry = 0
#     while retry < 3:
#         try:
#             sensor.measure()
            
#             break
#         except:
#             retry = retry + 1
#             print(".", end = "")
            
#     temp = (sensor.temperature())
#     hum = (sensor.humidity())
    
#     print(f"La temperatura es : {temp}")
#     print(f"La humedad es : {hum}")
    
#     if hum>=65:
#         relay.value(1)
#         print(f"Estado Relay {relay.value()}")
#     else:
#         relay.value(0)
#         print(f"Estado Relay {relay.value()}")
    
#     firebase.addto("palma/esp32_sensor/tracking", {"temperature": temp,"humidity":hum,"humidity_floor": hum_suelo_AC, "regular_light": luz_AC, "ambient_light": luz_amb_AC, "date": date},  bg=0)
#     firebase.put("palma/esp32_sensor/last_sinc", {"temperature": temp,"humidity":hum,"humidity_floor": hum_suelo_AC, "regular_light": luz_AC, "ambient_light": luz_amb_AC, "date": date}, bg=0)
    
#     #respuesta = urequests.get(url+"&field1="+str(temp)+"&field2="+str(hum)+"&field3="+str(hum_suelo_AC)+"&field4="+str(luz_AC)+"&field=5"+str(luz_amb_AC))
    
#     '''ESP32_Actuators\if hum_suelo_AC>=3000:
#         print("Humedad baja, abrir llave de riego")
#         open()
#     else:
#         print("Humedad alta, cerrar llave de riego")
#         close()'''
#     print("*"*32)
#     print(" ")
#     sleep(2)
    
