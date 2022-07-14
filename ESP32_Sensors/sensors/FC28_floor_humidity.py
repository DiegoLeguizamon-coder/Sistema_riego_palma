from machine import Pin as pin, ADC
from utime import sleep, sleep_ms

sensorAC=ADC(pin(32))
sensorAC.atten(ADC.ATTN_11DB)

def mapear(valor_sensor, minimo_entrada, maximo_entrada, minimo_salida, maximo_salida):
  valor_mapeado = (valor_sensor - minimo_entrada) * (maximo_salida - minimo_salida) / (maximo_entrada - minimo_entrada) + minimo_salida
  return valor_mapeado


def floor_humidity():
  hum_suelo_AC=sensorAC.read()
  return mapear(hum_suelo_AC,750,4095,100,0)


# while True:
#     hum_suelo_AC=sensorAC.read()
#     print("*"*32)
#     print(f"Humedad de suelo: {hum_suelo_AC}")
    
#     sleep(1)
#     print(f"Humedad de suelo: {hum_suelo_AC}%")
#     print("*"*32)