
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
json={'token':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJFbWFpbCI6InRlc3RAdGVzdC5jb20iLCJpc0FkbWluIjpmYWxzZX0.7d4LVnr43Od8tK7tcCdMMRoieXYD8xycLJBxxQxSDOU', 
        'userData':{
            'firstName':'new',
            'lastName':'new2'
        },
        'address':{
            'streetAddress':'newStreet',
            'state': 'newState',
            'country': 'newCountry',
        },
        'occupation':'newoccupation',
        'purposeOfUse':'NewUsage'
    
    }
req = requests.post('http://127.0.0.1:5000/api/updateProfile', json=json)
print(req.json())

##For GetProfile
req = requests.get('http://127.0.0.1:5000/api/getProfile', json={'token':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJFbWFpbCI6InRlc3RAdGVzdC5jb20iLCJpc0FkbWluIjpmYWxzZX0.7d4LVnr43Od8tK7tcCdMMRoieXYD8xycLJBxxQxSDOU'})
print(req.json())