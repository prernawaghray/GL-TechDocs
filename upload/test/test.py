import requests
import jwt
token  = jwt.encode({'user_id':'123456'},'c40bc9b7166c409aa25e84c06c79f2d7','HS256')
headers = {'x-access-tokens': token}
resp = requests.get('http://127.0.0.1:80', headers=headers)
print(resp.json())