from machine import Pin as pin

water_pump = pin(4, pin.OUT)

def state_water_pump(state):
    water_pump.value(state)
    
def validate_water_pump():
    return water_pump.value()