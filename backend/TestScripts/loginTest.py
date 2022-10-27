import requests
import sys


req = requests.post('http://127.0.0.1:5000/api/signin', json={'loginType':'email','username':'test3@test.com','password':'1234567', 'rememberMe':1})

print(req.json())
#eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJFbWFpbCI6InRlc3RAdGVzdC5jb20iLCJpc0FkbWluIjpmYWxzZX0.7d4LVnr43Od8tK7tcCdMMRoieXYD8xycLJBxxQxSDOU
