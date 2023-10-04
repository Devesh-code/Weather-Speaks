import requests
import json
import win32com.client

city = input("Enter city: ")

url = f"http://api.weatherapi.com/v1/current.json?key=d250a75cf1474c3ab7e184903230210&q={city}"
r = requests.get(url)
print("What do you want to know about today's weather?\n1. Temperature\n2. Humidity\n3. Wind\n4. Clouds\n")
x = int(input("Enter your choice: "))

match x:
    case 1:
        temp = json.loads(r.text)
        w = temp["current"]["temp_c"]
        speaker = win32com.client.Dispatch("SAPI.SpVoice")
        speaker.Speak(f"The current temperature in {city} is {w} degrees!")

    case 2:
        hu = json.loads(r.text)
        w = hu["current"]["humidity"]
        speaker = win32com.client.Dispatch("SAPI.SpVoice")
        speaker.Speak(f"The current humidity in {city} feels like {w}!")

    case 3:
        wind = json.loads(r.text)
        w = wind["current"]["wind_kph"]
        speaker = win32com.client.Dispatch("SAPI.SpVoice")
        speaker.Speak(f"The current wind in {city} is {w} kph!")

    case 4:
        c = json.loads(r.text)
        w = c["current"]["cloud"]
        speaker = win32com.client.Dispatch("SAPI.SpVoice")
        speaker.Speak(f"The current clouds in {city} is {w}!")

    case _:
        speaker = win32com.client.Dispatch("SAPI.SpVoice")
        speaker.Speak("Sorry, bro wrong input!")