import requests
import sys


req = requests.post('http://127.0.0.1:5000/api/signin', json={'loginType':'email','username':'test@test.com','password':'1234567', 'remember':True})

print(req.json())