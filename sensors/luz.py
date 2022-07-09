from machine import Pin as pin,ADC
from utime import sleep_ms

sensorAC=ADC(pin(34))
sensorAC.atten(ADC.ATTN_11DB)

while True:
    #hum_suelo_D = sensor.value()
    luz_normal_AC=sensorAC.read()
    sleep(1)
    print(f"Luz ambiental: {luz_AC}")