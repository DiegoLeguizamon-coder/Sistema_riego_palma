from machine import Pin as pin, ADC, PWM
from utime import sleep, sleep_ms

#sensor=pin(2, pin.IN)
sensorAC=ADC(pin(4))
sensorAC.atten(ADC.ATTN_11DB)

servo=PWM(pin(14), freq=50)

def mapear(valor_sensor, minimo_entrada, maximo_entrada, minimo_salida, maximo_salida):
  valor_mapeado = (valor_sensor - minimo_entrada) * (maximo_salida - minimo_salida) / (maximo_entrada - minimo_entrada) + minimo_salida
  return valor_mapeado

def open():
    for i in range(18,136):
        servo.duty(i)
        #   servo.duty16(i) Mayor presición
        sleep(0.1)

def close():
    for i in range(136,18,-1):
        servo.duty(i)
        sleep(0.1)


while True:
    hum_suelo_AC=sensorAC.read()
    #print(hum_suelo_AC)
    hum_suelo_AC=mapear(hum_suelo_AC,1000,4095,100,0)
    sleep(2)
    print(f"Humedad de suelo: {hum_suelo_AC}")
    
    if hum_suelo_AC<=0.0:
        print("Humedad baja, abrir llave de riego")
        open()
    else:
        print("Humedad alta, cerrar llave de riego")
        close()