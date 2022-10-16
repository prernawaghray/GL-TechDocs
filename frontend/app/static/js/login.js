
$(document).ready(function() {
    $('#email-login').on('submit', function(event) {
       loginButtonClicked();
       event.preventDefault();
// keeping this commented for now as Sreenivas sir is writing request response based implementation        
     
     });
});


function saveTokenInSession(AUT)
{
    $.ajax({
        data:{
            authToken:AUT
        },
        type:'POST',
        url:getFrontEndUrl('saveUserToken'),
        success:function(data)
        {
            window.location.replace('/dashboard');
        }
    }

    );
}

function loginButtonClicked()
{
    removeAlert('#email-login-errorMessage');
    try{
    $.ajax({
        data : {
           email : $('#email-input').val(),
           password: $('#password-input').val(),
               },
           type : 'POST',
           url : getApiUrl('login'),
           success: function(data) {
            //In case of success the data contains the JSON

            if(data.status==true)
            {
                localStorage.setItem('userToken', data.authToken);
                saveTokenInSession(data.authToken);
                
            }
            else
            {
                showAlert('#email-login-errorMessage', 'alert-warning', "Login!!", data.message);
              
            }
            
            
          },
          error:function(data) {
            // in case of error we need to read response from data.responseJSON
            showAlert('#email-login-errorMessage', 'alert-danger', "Login!!", data.responseJSON.message);

            
          }
        }
          );
    }
    catch(e)
    {
        console.log(e)
    }
}