from machine import Pin as pin
from utime import sleep
from modules.WiFi_connection import connect_Wifi
from services.firebase_service import get_last_register
from actuators.relay_water_pump import state_water_pump, validate_water_pump
import sensors.water_flow

led = pin(2, pin.OUT)

print('Conectando '+" …")
if  not connect_Wifi("Tech_001", "1019077632"):
    print("Error al conectar")
else :
    led.value(1)
    print("Conexión exitosa!")
    
while True:
    last_sync = get_last_register()
    
    if last_sync['humidity_floor'] <= 30:
        state_water_pump(1)
        print("Bomba encendida")
    else:
        print("Bomba apagada")
        state_water_pump(0)
        
    sleep(5)