import requests

# Test /file/create
# Creates a new file
res = requests.post('http://127.0.0.1:5000/file/create', json={"UserId":"u123"})
print(res.json())
# output will be 
# {'data': '{"DocumentId": 4, "Filename": "untitled_20221011212801.tex", "UserId": "u123", "body": ""}', 'message': 'success'}




