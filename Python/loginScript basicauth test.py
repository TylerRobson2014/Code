import requests
from requests.auth import HTTPBasicAuth

url = 'http://pentesteracademylab.appspot.com/lab/webapp/basicauth'
USERNAME = 'admin' 
PASSWORD = 'aaaaa'
a = ['a','s','d']
x = ['a','a','a','a','a']
listToTry = [0]*(5*5*5*5*5)
i = 0

PASSWORD = 'aaddd'
requests.Session().get(url)
payload = {'email': USERNAME,'password': PASSWORD}
login_data = dict(username=USERNAME,password=PASSWORD)
p = requests.Session().post(url,auth =(USERNAME,PASSWORD))
i= i+1
if "Unauthorized" in p.content:
	print i,PASSWORD,"Failed"
else:
	print i,PASSWORD,"***************** Sucess **********************"
				

	
	
