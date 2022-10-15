$( function() {
    $( "#accordion" ).accordion({heightStyle: 'panel',collapsible:true});
  } );

$(document).ready(function() {
    loadProfileData();
    $('#profileForm').on('submit', function(event) {
       profileUpdate();
       event.preventDefault();
     
     });
});

function updateProfile(data)
{
    $('#first-name').val(data.firstName);
    $('#last-name').val(data.lastName);
}
function loadProfileData()
{
    try{
        $.ajax({
            data : {
               authToken : getUserToken()
                   },
               type : 'POST',
               url : getApiUrl('getProfile'),
               success: function(data) {
                //In case of success the data contains the JSON
    
                if(data.status==true)
                {
                    updateProfile(data.userData);
                }
                else
                {
                    showAlert('#profile-errorMessage','alert-warning',"Profile Update!!",data.message);
                    
                }
                
                
              },
              error:function(data) {
                // in case of error we need to read response from data.responseJSON
                showAlert('#profile-errorMessage','alert-danger',"Profile Update!!",data.responseJSON.message);
                
                
              }
            }
              );
        }
        catch(e)
        {
            console.log(e)
        }
}


function profileUpdate()
{
    try{
        $.ajax({
                data : {
                    authToken:localStorage.getItem('userToken'),
                    userData:
                            {
                                firstName:$('#first-name').val(),
                                lastName:$('#last-name').val(),
                            }

                },
                type : 'POST',
                url : getApiUrl('updateProfile'),
                success: function(data) {
                //In case of success the data contains the JSON
    
                if(data.status==true)
                {
                    showAlert('#profile-errorMessage','alert-success',"Profile Update!!","Successfully updated");
                }
                else
                {
                    showAlert('#profile-errorMessage','alert-warning',"Profile Update!!",data.message);

                    //showError(data.responseJSON.message,'Profile Update')
                   
                }
                
                
              },
              error:function(data) {
                // in case of error we need to read response from data.responseJSON
                showAlert('#profile-errorMessage','alert-danger',"Profile Update!!",data.responseJSON.message);
                
              }
            }
              );
        }
        catch(e)
        {
            console.log(e)
        }
}