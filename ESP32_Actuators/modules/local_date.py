import urequests
import ujson

def take_time():
    url = "http://worldtimeapi.org/api/timezone/America/Bogota"

    response = urequests.get(url)
    jsonResponse = response.json()
    date = str(jsonResponse["datetime"])
    year = date[0:4]
    month = date[5:7]
    day = date[8:10]
    hour = date[11:13]
    minute = date[14:16]
    seconds = date[17:19]
    current_date = year + "-" + month + "-" + day + " " + hour + ":" + minute + ":" + seconds 
    return current_date