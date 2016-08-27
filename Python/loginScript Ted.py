import requests
from requests.auth import HTTPBasicAuth

url = 'https://google-gruyere.appspot.com/550568524735/login'
USERNAME = 'Ted' 
PASSWORD = 'password'

requests.Session().get(url)
payload = {'uid': USERNAME,'pw': PASSWORD}
login_data = dict(uid=USERNAME,pw=PASSWORD)
p = requests.get(url,params=payload)
print p.content

				

	
	
