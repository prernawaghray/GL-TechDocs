
$(document).ready(function() {
    $('#email-login').on('submit', function(event) {
       loginButtonClicked();
        event.preventDefault();
// keeping this commented for now as Sreenivas sir is writing request response based implementation        
     
     });
});


function loginButtonClicked()
{
    try{
    $.ajax({
        data : {
           email : $('#email-input').val(),
           password: $('#password-input').val(),
               },
           type : 'POST',
           url : '/api/login',
           success: function(data) {
            if(data.status==true)
            {
                window.location.replace('/dashboard')
            }
            else
            {
                $('#email-login-errorMessage').text(data.message);
            }
            console.log(data);
            
          },
          error:function(data) {
            console.log(data);
            
          }
        }
          );
    }
    catch(e)
    {
        console.log(e)
    }
}