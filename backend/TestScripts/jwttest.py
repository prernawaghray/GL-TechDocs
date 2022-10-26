import requests

req = requests.post('http://127.0.0.1:5000/api/signout', json={'token':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJFbWFpbCI6InRlc3RAdGVzdC5jb20iLCJpc0FkbWluIjpmYWxzZX0.7d4LVnr43Od8tK7tcCdMMRoieXYD8xycLJBxxQxSDOU'})
print(req.json())