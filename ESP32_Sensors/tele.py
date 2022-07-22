#------------------------------ [IMPORT]------------------------------------
import network, time, urequests,utime
from machine import Pin, ADC, PWM
from utelegram import Bot
TOKEN = '5317120366:AAFMlC8KY6wXyyIm7P7y4xs1mdODnEBDYqY'
#--------------------------- [OBJETOS]---------------------------------------
bot = Bot(TOKEN)
bombillo  = Pin(5, Pin.OUT)
pot = ADC(Pin(35))
led = Pin(2, Pin.OUT)
#----------------------[ CONECTAR WIFI ]---------------------------------------------------------#
def conectaWifi (red, password):
      global miRed
      miRed = network.WLAN(network.STA_IF)     
      if not miRed.isconnected():              #Si no está conectado…
          miRed.active(True)                   #activa la interface
          miRed.connect(red, password)         #Intenta conectar con la red
          print('Conectando a la red', red +"…")
          timeout = time.time ()
          while not miRed.isconnected():           #Mientras no se conecte..
              if (time.ticks_diff (time.time (), timeout) > 10):
                  return False
      return True
#------------------------------------[BOT]---------------------------------------------------------------------#
if conectaWifi ("Tech_001", "1019077632"):
    print ("Conexión exitosa!")
    print('Datos de la red (IP/netmask/gw/DNS):', miRed.ifconfig())
    
    @bot.add_message_handler("Hola")
    def help(update):
        update.reply('''¡Bienvenido!\n
                     Menu Principal\n Ejemplo\n Elije una opción :
                     Nombre  : 1 \nEdad: 2\nEstado Civil: 3
                     No olvides que estoy para ayudarte''')
        led.value(1)
    
    @bot.add_message_handler("Nombre")
    def help(update):
        update.reply('''Nombre: Javier Moreno
                     No olvides que estoy para ayudarte''')



    @bot.add_message_handler("Edad")
    def help(update):
        update.reply('''22 Años''')



    @bot.add_message_handler("Estado civil")
    def help(update):
        update.reply('''Estoy Soltero''')                 
    @bot.add_message_handler("potenciometro")
    def help(update):
        potenciometro=pot.read()
        print (f"el valor del potenciometro es: {potenciometro} ")
        update.reply(f'el valor del potenciometro es {potenciometro}')      
    bot.start_loop()
else:
       print ("Imposible conectar")
       miRed.active (False)

