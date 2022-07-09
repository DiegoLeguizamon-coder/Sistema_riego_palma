from machine import Pin as pin, PWM
from utime import sleep

servo=PWM(pin(14), freq=50)

def mapear(valor_sensor, minimo_entrada, maximo_entrada, minimo_salida, maximo_salida):
    valor_mapeado = (valor_sensor - minimo_entrada) * (maximo_salida - minimo_salida) / (maximo_entrada - minimo_entrada) + minimo_salida
    return valor_mapeado


# Rango del servo 18 - 136
def prueba():
#  izq->der
    for i in range(18,136):
        servo.duty(i)
        #   servo.duty16(i) Mayor presición
        print(i)
        sleep(0.1)
# der-> izq
    '''for i in range(136,18,-1):
        servo.duty(i)
        print(i)
        sleep(0.1)'''
        
prueba()
        


'''while True:
    angulo=float((input("ingrese el angulo"))
    if angulo>=0 and angulo<=180:
        angulo=mape(angulo,0,180,0,1023)
    else:
        print("Ángulo no valido para el servo")'''