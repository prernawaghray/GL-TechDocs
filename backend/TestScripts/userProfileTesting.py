
# {authToken:"xxxxxxxxxxxxx",
# userData:{
#             firstName:"ghjgjg",
#             lastName:"jhjghjg"
#           },
# address : {
#             streetAddress: "xxxx",
#              state:"yyyy",
#              country:"zzzz"
#             },
#              occupation: "ooooo",
#              purposeOfUse:"pppp"
#             }                      
# }

##For updateProfile
import requests
json={ 
        'userData':{
            'firstName':'new',
            'lastName':'new2'
        },
        'address':{
            'streetAddress':'newStreeatt',
            'state': 'newSte',
            'country': 'newCountry',
        },
        'occupation':'newoccupation',
        'purposeOfUse':'NewUsage'
    
    }
headers = {"authToken":'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJFbWFpbCI6InRlc3RAdGVzdC5jb20iLCJpc0FkbWluIjpmYWxzZX0.7d4LVnr43Od8tK7tcCdMMRoieXYD8xycLJBxxQxSDOU'}
req = requests.post('http://127.0.0.1:5000/api/updateProfile', json=json, headers=headers)
print(req.json())

##For GetProfile
req = requests.post('http://127.0.0.1:5000/api/getProfile', headers=headers)
print(req.json())