from machine import Pin as pin, ADC, PWM, Timer
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

import modules.utelegram as telegram
from config.config import utelegram_config

url = "https://api.thingspeak.com/update?api_key=OVCEZPSQVOMLSKKG"
temporary_task_TS = Timer(1)
temporary_task_Tele= Timer(0)

def sensor_data():
    global s_f_humidity
    global s_humidity
    global s_temperature
    global s_light
    global date
    s_f_humidity = floor_humidity()
    s_humidity = humidity()
    s_temperature = temperature()
    s_light = ambient_light()
    global measurements
    
    date = take_time()
    
    measurements = {
        "temperature": s_temperature,
        "humidity":s_humidity,
        "humidity_floor": s_f_humidity,
        "ambient_light": s_light,
        "date": date
        }
    
def loop_sensor_TS(Timer):
    sensor_data()
    print("%"*32)
    print(f"Current date: {date}")
    print("--x--x--"*4)
    print(f"Humedad de suelo: {s_f_humidity}%")
    print(f"Humedad: {s_humidity}%")
    print(f"Temperatura: {s_temperature}C")
    print(f"Luz ambiente: {s_light}%")
            
    response = urequests.get(url+"&field1="+str(s_light)+"&field2="+str(s_humidity)+"&field3="+str(s_f_humidity)+"&field4="+str(s_temperature))
    print(f"Response TS: {response.status_code , response.text}")
    response.close()
    print("Se cierra la conexión de Thinkspeak")
    measurements = {
        "temperature": s_temperature,
        "humidity":s_humidity,
        "humidity_floor": s_f_humidity,
        "ambient_light": s_light,
        "date": date
        }
        #request_url = "https://backend.thinger.io/v3/users/DiegoLeguizamon/devices/esp_3201/callback/data"
        #header_data = { "content-type": 'application/json', "Authorization": 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJEZXZpY2VDYWxsYmFja19lc3BfMzIwMSIsInN2ciI6InVzLWVhc3QuYXdzLnRoaW5nZXIuaW8iLCJ1c3IiOiJEaWVnb0xlZ3VpemFtb24ifQ.CRu0RlSpxtg9DeVERs9E3i-shaqnDJTQcnnAIBLzTdQ'}
        #response = urequests.post(request_url, headers = header_data, data = measurements)
        #print(f"Response TS: {response.status_code , response.text}")
            
    print("%"*32)
    sleep(1)
            
    update_last_register(measurements)
    register_measurements(measurements)
    
    
def loop_sensor_firebase(Timer):
    sensor_data()
    print("%"*32)
    print(f"Current date: {date}")
    print("--x--x--"*4)
    print(f"Humedad de suelo: {s_f_humidity}%")
    print(f"Humedad: {s_humidity}%")
    print(f"Temperatura: {s_temperature}C")
    print(f"Luz ambiente: {s_light}%")
        
    response = urequests.get(url+"&field1="+str(s_light)+"&field2="+str(s_humidity)+"&field3="+str(s_f_humidity)+"&field4="+str(s_temperature))
    print(f"Response TS: {response.status_code , response.text}")
    
    measurements = {
        "temperature": s_temperature,
        "humidity":s_humidity,
        "humidity_floor": s_f_humidity,
        "ambient_light": s_light,
        "date": date
        }
    
    #request_url = "https://backend.thinger.io/v3/users/DiegoLeguizamon/devices/esp_3201/callback/data"
    #header_data = { "content-type": 'application/json', "Authorization": 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJEZXZpY2VDYWxsYmFja19lc3BfMzIwMSIsInN2ciI6InVzLWVhc3QuYXdzLnRoaW5nZXIuaW8iLCJ1c3IiOiJEaWVnb0xlZ3VpemFtb24ifQ.CRu0RlSpxtg9DeVERs9E3i-shaqnDJTQcnnAIBLzTdQ'}
    #response = urequests.post(request_url, headers = header_data, data = measurements)
    #print(f"Response TS: {response.status_code , response.text}")
        
    print("%"*32)
    sleep(1)
        
    update_last_register(measurements)
    register_measurements(measurements)
    

def get_message(message):
    # bot.send(message['message']['chat']['id'], message['message']['text'].upper())
    bot.send(message['message']['chat']['id'],"Comando no reconocido, por favor, intente con los siguientes comandos: \n\n\n" +
             "encender -> Para encender el ventilador \n" +
             "apagar    -> Para apagar el ventilador \n" +
             "datos     -> Obtener datos de los  sensores \n")
    
def turn_off_ventilator(message):
    print(message)
    bot.send(message['message']['chat']['id'], "Ventilador apagado")
    relay_ven.state_ventilator(0)
    

def turn_on_ventilator(message):
    print(message)
    bot.send(message['message']['chat']['id'], "Ventilador encendido")
    relay_ven.state_ventilator(1)
    
def send_data(message):
    sensor_data()
    print(message)
    bot.send(message['message']['chat']['id'], "La temperatura es: " + str(measurements['temperature']) 
             + ",\n la humedad del suelo es: " + str(measurements['humidity_floor']) 
             + ",\n la humedad del ambiente es: " + str(measurements['humidity']) 
             + ",\n la iluminacion del ambiente es: " + str(measurements['ambient_light']) 
             + ",\n fecha de dato: " + str(measurements['date']))
    
def create_bot():
    print("bot creado")
    global bot
    bot = telegram.ubot(utelegram_config['token'])
    bot.register('encender', turn_on_ventilator)
    bot.register('apagar', turn_off_ventilator)
    bot.register('datos', send_data)
    bot.set_default_handler(get_message)
    
create_bot()

def activate_bot(Timer):
    date = take_time()
    print(f"bot_date{date}")

    print('BOT LISTENING')
    bot.listen()

if not connectWifi("Tech_001", "1019077632"):
    print("Error al conectar a la red.")
else:
    print("Conexión exitosa.")
    

temporary_task_Tele.init(mode=Timer.PERIODIC, period=4000, callback=activate_bot)
temporary_task_TS.init(mode=Timer.PERIODIC, period=2000, callback=loop_sensor_TS)

print("Llegó acá")