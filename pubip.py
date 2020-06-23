"""
    74 6F 62

    author:tob
    desc: write public ip and said ip location

"""

import requests
import json

def get_public_ip():
    response = requests.get("http://whatismyip.akamai.com/")
    print(f"Your public IP Address is {response.text}")
    return response.text

def get_ip_geoloc(ip):
    session = requests.Session()
    uri = f"https://tools.keycdn.com/geo.json?host={ip}"
    session.headers.update({ 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36' })
    response = session.get(uri)
    json_response = json.loads(response.text)
    country = json_response["data"]["geo"]["country_name"]
    city = json_response["data"]["geo"]["city"]
    region = json_response["data"]["geo"]["region_name"]
    lat = json_response["data"]["geo"]["latitude"]
    long = json_response["data"]["geo"]["longitude"]
    print(f"\nCountry: {country}\nCity: {city}\nRegion: {region}\nCoordinates: {lat},{long}")
    
ipaddr = get_public_ip()
get_ip_geoloc(ipaddr)