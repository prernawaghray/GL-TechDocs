/* this logoutButtonClicked function checks for the userToken in local Storage
   if JWT is i local storage it removes it sends JWT to backend for validation
   if it is valid redirects to home page after logout
   if it is invalid or not in local storage, it issues a "bad requests" alert and 
   redirects to home page*/

   
async function logoutButtonClicked()
{
    
    userToken = localStorage.getItem('userToken');
    
    if (userToken !== null){
        localStorage.removeItem('userToken');

        await fetch(getApiUrl('signout'), {
            method: 'post',
            headers:{
                'Content-Type':'application/json',
                'authToken': userToken,
            }
        })
        .then(response => { if(response.status == 400) {
                                window.alert('bad request');
                            }})
        // .then(data => {console.log(data))
        .catch(error => {console.log(error)})
    }

    else{
        window.alert('bad request');
    }
    window.location.replace('/');
}