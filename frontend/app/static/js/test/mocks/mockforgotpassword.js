
import { isEqualObjects,baseApiUrl } from "../helpers.js";
export {mockhandlers};
var forgotPasswordApiUrl = baseApiUrl + "forgot-password";
var successfulAuthToken = "123456"
var successfulForgotPasswordRequest = { 
    
  email_id:'admin@techdocs.com'   
}



var successfulForgotPasswordResponse = {
    
                      
    message: "Sent a reset pwd link to email ID" 
    
}

var successfulForgotPasswordFailure = {
    
                      
  message: "User account not found" 
  
}

var mockforgotPasswordSuccess={
    url: forgotPasswordApiUrl,
    data: function( data ) {
        return isEqualObjects( data, successfulForgotPasswordRequest ) ;
      },
    status:200,
    responseText:successfulForgotPasswordResponse
  };

  var mockforgotPasswordFailure={
    url: forgotPasswordApiUrl,
    data: function( data ) {
        return !(isEqualObjects( data, successfulForgotPasswordRequest ) );
      },
    status:401,
    responseText:successfulForgotPasswordFailure
  };
  
  var mockhandlers=
    [mockforgotPasswordSuccess,
      mockforgotPasswordFailure

    ];
  
