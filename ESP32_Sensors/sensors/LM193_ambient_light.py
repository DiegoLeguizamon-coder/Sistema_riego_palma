from machine import Pin as pin,ADC

sensorAC=ADC(pin(34))
sensorAC.atten(ADC.ATTN_11DB)

def mapear(valor_sensor, minimo_entrada, maximo_entrada, minimo_salida, maximo_salida):
  valor_mapeado = (valor_sensor - minimo_entrada) * (maximo_salida - minimo_salida) / (maximo_entrada - minimo_entrada) + minimo_salida
  return valor_mapeado

def ambient_light():
    s_light = sensorAC.read()
    return mapear(s_light, 1400, 4095, 100, 0)