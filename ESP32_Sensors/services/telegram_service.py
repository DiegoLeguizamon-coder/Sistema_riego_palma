from config.config import utelegram_config
from config.config import wifi_config
import modules.utelegram as telegram

turn_on = 'encender'
bot = telegram.ubot(utelegram_config['token'])


def get_message(message):
    # bot.send(message['message']['chat']['id'], message['message']['text'].upper())
    bot.send(message['message']['chat']['id'],"Comando no reconocido, por favor, intente con los siguientes comandos: \n" +
             "  encender -> Para encender el ventilador \n" +
             "  apagar   -> Para apagar el ventilador \n" +
             "  datos    -> Obtener datos de los sensores \n")
    
def turn_off_ventilator(message):
    print(message)
    bot.send(message['message']['chat']['id'], "Esta apagado")

def turn_on_ventilator(message):
    print(message)
    bot.send(message['message']['chat']['id'], "Esta encendido")
    
def send_data(message, measurements):
    print(message)
    bot.send(message['message']['chat']['id'], "La temperatura es: " + str(measurements['temperature']) + ",\n la humedad del suelo es: " + str(measurements['humidity_floor']) + ",\n la humedad del ambiente es: " + str(measurements['humidity'])+ ",\n la iluminacion del ambiente es: " + str(measurements['ambient_light'])+ ",\n fecha de dato: " + str(measurements['date']))
    

def activate_bot():
    
    bot.register(turn_on, turn_on_ventilator)
    bot.register('apagar', turn_off_ventilator)
    bot.register('datos', send_data)
    bot.set_default_handler(get_message)

    print('BOT LISTENING')
    bot.listen()
    return true