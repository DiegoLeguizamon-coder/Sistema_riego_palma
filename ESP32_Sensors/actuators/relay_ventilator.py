from machine import Pin as pin

relay = pin(4, pin.OUT)

def state_ventilator(state):
    relay.value(state)
    
def validate_ventilator():
    return relay.value()
