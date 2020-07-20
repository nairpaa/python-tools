#!/bin/python3

# Gathering Information - Grabbing Banners, Hostname and IP Lookup

import sys
import requests
import socket
import json

if len(sys.argv) < 2:
    print("Usage: " + sys.argv[0] + " <url>")
    sys.exit(1)

# get response headers 
req = requests.get("https://" + sys.argv[1])
print("\n" + str(req.headers))

# get ip from the domain
gethostby_ = socket.gethostbyname(sys.argv[1])
print("\nThe IP Address of " + sys.argv[1] + " is: " + gethostby_ + "\n")

# looking for information about the IP from ipinfo.io
req_two = requests.get("https://ipinfo.io/" + gethostby_ + "/json")
resp_ = json.loads(req_two.text)

print("Location: " + resp_["loc"])
print("Region : " + resp_["region"])
print("City : " + resp_["city"])
print("Country : " + resp_["country"])