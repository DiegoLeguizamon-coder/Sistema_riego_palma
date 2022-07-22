import modules.ufirebase as firebase

url = "https://curso-android-firebase-6ae58-default-rtdb.firebaseio.com/"
path_last_sync = "palma/esp32_sensor/last_sinc"
path_tracking = "palma/esp32_sensor/tracking"

firebase.setURL(url)

def update_last_register(measurements):
    firebase.put(path_last_sync, {"temperature": measurements['temperature'],
                                  "humidity":measurements['humidity'],
                                  "humidity_floor": measurements['humidity_floor'],
                                  "ambient_light": measurements['ambient_light'],
                                  "date": measurements['date']}, bg=0)
    
    
def register_measurements(measurements):
    firebase.addto(path_tracking, {"temperature": measurements['temperature'],
                                  "humidity":measurements['humidity'],
                                  "humidity_floor": measurements['humidity_floor'],
                                  "ambient_light": measurements['ambient_light'],
                                  "date": measurements['date']}, bg=0)
