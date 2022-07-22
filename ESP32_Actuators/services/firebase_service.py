import ufirebase as firebase

url = "https://curso-android-firebase-6ae58-default-rtdb.firebaseio.com/"
path_last_sync = "palma/esp32_sensor/last_sinc"
path_tracking = "palma/esp32_sensor/tracking"

firebase.setURL(url)

def get_last_register():
    firebase.get(path_last_sync, "last_sync", bg=0)
    return firebase.last_sync
