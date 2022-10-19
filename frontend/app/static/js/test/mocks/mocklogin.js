
import { isEqualObjects,baseApiUrl } from "../helpers.js";
export {mockhandlers};
var loginApiUrl = baseApiUrl + "login";
var successfulLoginData = {
    email:'admin@techdocs.com', 
    password : 'admin123'
}
var successfulAuthToken = "123456"
var loginResponseSuccess = {
    status:true,
    authToken: successfulAuthToken,
    message:"Logged in successfully"
}
var loginResponseFailure = {
    status:false,
    authToken:null,
    message:"MOCK : Invalid userid or password"
}
var mockLoginSuccess={
    url: loginApiUrl,
    data: function( data ) {
        return isEqualObjects( data, successfulLoginData );
      },
    status:200,
    responseText:loginResponseSuccess
  };

  var mockLoginFailure={
    url: loginApiUrl,
    data: function( data ) {
        return !isEqualObjects( data, successfulLoginData );
      },
    status:401,
    responseText:loginResponseFailure
  };
  
  var mockhandlers=
    [mockLoginSuccess,
     mockLoginFailure
    ];
  
