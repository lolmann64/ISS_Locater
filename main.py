import requests
import folium
import time
import sys


def exit_program():         #exit
    print("AAAAAAAAAAAA brumbejondödnalndasd")
    sys.exit(0)

def acquire_iss_location():     #location der ISS herrausfinden durch API
    response = requests.get("http://api.open-notify.org/iss-now.json")
    data = response.json()
    latitude = float(data["iss_position"]["latitude"])
    longitude = float(data["iss_position"]["longitude"])
    return latitude, longitude
iss_latitude, iss_longitude = acquire_iss_location()
print(f"ISS aktueller Standort:\n Latitude: {iss_latitude}, Longitude: {iss_longitude}")

def generate_iss_map(latitude, longitude):      #map generieren mit folium. Latitude und Longitude parameter mitgegeben
    iss_map = folium.Map(location=[latitude, longitude], zoom_start=2)
    folium.Marker([latitude, longitude], tooltip="ISS hiieeeeerrrr!!", popup="International Space Station", icon=folium.Icon(color="green", icon="star")).add_to(iss_map)
    return iss_map

while True:     #automatisirung. Ertslle X sekunden eine map und poste standort
    iss_latitude, iss_longitude = acquire_iss_location()
    print(f"ISS aktueller Standort:\n Latitude: {iss_latitude}, Longitude: {iss_longitude}")
    iss_map = generate_iss_map(iss_latitude, iss_longitude)
    iss_map.save("iss_map.html")
    #print("XuXuXuXuXUXu")
    time.sleep(24)

    user_input = input("Would you like to quit the program? (y/n):  ")
    if user_input == "y":
        print(f"ISS aktueller Standort:\n Latitude: {iss_latitude}, Longitude: {iss_longitude}")
        exit_program()
