import urllib.parse
import requests

main_api = "http://ip-api.com/json/"

json_data = requests.get(main_api).json()

if json_data["status"] == "success":
    print("IP: " + (json_data["query"]))
    print("Your Internet service provider is: " + (json_data["isp"]) + " | Their AS#: " + (json_data["as"]))
    print("Your location is: " + (json_data["country"]) + ", " + (json_data["region"]) + ", " + (json_data["city"]) + ", " + (json_data["zip"]))
    print("Your cordinates are: " + str(json_data["lat"]) + ", " + str(json_data["lon"]))
else:
    print("Check your ethernet connection.")
