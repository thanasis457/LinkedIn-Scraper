from  linkedin_api import Linkedin
from getpass import getpass
import re

print("Enter your email:")
email = input()
password = getpass('Enter your password:')
api = None
try:
    api = Linkedin(username=email, password=password)
except:
    print('Could not login')
    

def get_profile(url):
    profile = re.search('in/([A-Za-z0-9\-]*)/.*', url)
    print(profile)
    if(profile == None):
        raise Exception('Bad url format')
    profile = api.get_profile(profile.group(1))
    return profile