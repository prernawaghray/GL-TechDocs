
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
    loginFormData = {
        loginType : "email",
        email : $('#email-input').val(),
        password: $('#password-input').val(),
        rememberMe : $('#remember-me').prop("checked")?1:0
            };
    callLoginApi(loginFormData);
}

function callLoginApi(loginFormData)
{
    removeAlert('#email-login-errorMessage');
    try{
    $.ajax({
        data : loginFormData,
           type : 'POST',
           url : getApiUrl('login'),
           success: function(data) {
            //In case of success the data contains the JSON

            
                localStorage.setItem('userToken', data.authToken);
                saveTokenInSession(data.authToken);
            
            
            
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
var googleLoginButtonOptions=
{ theme: 'filled_blue', 
size: 'large',
width:380};

function handleGoogleAuthResponse(token) {
    var response = parseJwt(token.credential);
    console.log(response); 
    loginFormData = {
        loginType : "google",
        email : response.email,
        password: "authenticated",
        rememberMe : 0
            };
    callLoginApi(loginFormData);
    
  }

  window.onload = function () {
    google.accounts.id.initialize({
      client_id: getClientId(),
      callback: handleGoogleAuthResponse,
      prompt_parent_id:"googleLogin"
    });
   
    google.accounts.id.renderButton($('#googleLogin')[0],googleLoginButtonOptions);
    
  };