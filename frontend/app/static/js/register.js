
$(document).ready(function() {
  console.log("ready")
    $('#register-form').on('submit', function(event) {
        console.log("register")
        event.preventDefault();
        if ($('#password-input').val() != $('#password_confirm-input').val()) {
           showAlert('#register-errorMessage', 'alert-danger', "Error:","Password and confirm password should match!!");
           return;
        }
       registerButtonClicked();
     
     });
});


function registerButtonClicked() {
    registerFormData = {
        "loginType" : "email",
        "FirstName" : $('#firstname-input').val(),
        "LastName" : $('#lastname-input').val(),
        "email" : $('#email-input').val(),
        "password" : $('#password-input').val()
//        confirmPassword: $('#password_confirm-input').val()
    };
    console.log(JSON.stringify(registerFormData))
    callLoginApi(registerFormData);
}

function callLoginApi(registerFormData) {
    removeAlert('#register-errorMessage');
    try {
    $.ajax({
           data : JSON.stringify(registerFormData),
           contentType:"application/json; charset=utf-8",
           type : 'POST',
           dataType: "json",
           url : getApiUrl('register'),
           success: function(data) {
            //In case of success the data contains the JSON
            
            console.log("Registered successfully!!")
            showAlert('#register-infoMessage', 'alert-info', "", "Your are registered successfully!!");

          },
          error:function(data) {
            // in case of error we need to read response from data.responseJSON
            showAlert('#register-errorMessage', 'alert-danger', "Register!!", getResponseMessage(data));

            
          }
        });
    } catch(e) {
        console.log(e)
    }
}

var googleLoginButtonOptions=
{ 
  theme: 'filled_blue', 
  size: 'large',
  width:380
};

function handleGoogleAuthResponse(token) {
    var response = parseJwt(token.credential);
    console.log(response); 
    registerFormData = {
        loginType : "google",
        email : response.email,
        password: "authenticated",
        rememberMe : 0
            };
    callLoginApi(registerFormData);
    
  }

  window.onload = function () {
    google.accounts.id.initialize({
      client_id: getClientId(),
      callback: handleGoogleAuthResponse,
      prompt_parent_id:"googleLogin"
    });
   
    google.accounts.id.renderButton($('#googleLogin')[0],googleLoginButtonOptions);
    
  };