from machine import Pin as pin, ADC
from utime import sleep, sleep_ms

#sensor=pin(2, pin.IN)
sensorAC=ADC(pin(32))
sensorAC.atten(ADC.ATTN_11DB)

def mapear(valor_sensor, minimo_entrada, maximo_entrada, minimo_salida, maximo_salida):
  valor_mapeado = (valor_sensor - minimo_entrada) * (maximo_salida - minimo_salida) / (maximo_entrada - minimo_entrada) + minimo_salida
  return valor_mapeado


while True:
    #hum_suelo_D = sensor.value()
    hum_suelo_AC=sensorAC.read()
    #print(hum_suelo_AC)
    print("*"*32)
    print(f"Humedad de suelo: {hum_suelo_AC}")
    hum_suelo_AC=mapear(hum_suelo_AC,0,4095,100,0)
    sleep(1)
    print(f"Humedad de suelo: {hum_suelo_AC}%")
    print("*"*32)