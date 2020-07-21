import requests 
import sys

sub_list = open("subdomains-100.txt") # https://github.com/rbsec/dnscan/
subs = sub_list.readlines()

for sub in subs:
    url_to_check = f"http://{sub}.{sys.argv[1]}"

    try:
        requests.get(url_to_check)
    
    except requests.ConnectionError:
        pass

    else:
        print("Valid domain: ", url_to_check)