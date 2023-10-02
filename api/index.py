import urllib.parse
import requests
from http.server import BaseHTTPRequestHandler

main_api = "http://ip-api.com/json/"

json_data = requests.get(main_api).json()
 
class handler(BaseHTTPRequestHandler):
 
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        if json_data["status"] == "success":
            self.wfile.write("IP: " + (json_data["query"]))
            self.wfile.write("Your Internet service provider is: " + (json_data["isp"]))
            self.wfile.write("ISP AS#: " + (json_data["as"]))
            self.wfile.write("Your location is: " + (json_data["country"]) + ", " + (json_data["region"]) + ", " + (json_data["city"]) + ", " + (json_data["zip"])))
            self.wfile.write("Your cordinates are: " + str(json_data["lat"]) + ", " + str(json_data["lon"]))
        else:
            self.wfile.write("Check your ethernet connection.")
        return


