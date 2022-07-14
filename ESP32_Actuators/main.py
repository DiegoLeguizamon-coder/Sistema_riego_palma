from machine import Pin as pin
from modules.WiFi_connection import connect_Wifi
# import ufirebase as firebase

# firebase.setURL("https://curso-android-firebase-6ae58-default-rtdb.firebaseio.com/")
led = pin(2, pin.OUT) 

print('Conectando '+" …")
if  not connect_Wifi("Tech_001", "1019077632"):
    print("Error al conectar")
else :
    led.value(1)
    print("Conexión exitosa!")