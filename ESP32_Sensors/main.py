from machine import Pin as pin, ADC, PWM
from utime import sleep, sleep_ms, time
import network, time, urequests
import ujson
import random
from modules.WiFi_connection import connectWifi
from modules.local_date import take_time
from services.firebase_service import update_last_register, register_measurements
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
    date = take_time()
    print("%"*32)
    print(f"Current date: {date}")
    print("--x--x--"*4)
    print(f"Humedad de suelo: {s_f_humidity}%")
    print(f"Humedad: {s_humidity}%")
    print(f"Temperatura: {s_temperature}C")
    print(f"Luz ambiente: {s_light}%")
    
    print("%"*32)
    sleep(30)
    '''if relay_ven.validate_ventilator()== 1 :
        relay_ven.state_ventilator(0)
    else: 
        relay_ven.state_ventilator(1)'''
    
    measurements = {
        "temperature": s_temperature,
        "humidity":s_humidity,
        "humidity_floor": s_f_humidity,
        "ambient_light": s_light,
        "date": date
        }
    
    update_last_register(measurements)
    register_measurements(measurements)
    
