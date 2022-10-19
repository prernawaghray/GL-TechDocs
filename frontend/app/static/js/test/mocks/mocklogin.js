
import { isEqualObjects,baseApiUrl } from "../helpers.js";
export {mockhandlers};
var loginApiUrl = baseApiUrl + "login";
var successfulAuthToken = "123456"
var successfulLoginRequest = { 
    loginType:"email",
    email:'admin@techdocs.com', 
    password : 'admin123',
    rememberMe : 1
}

var successfulLoginRequestGoogle = { 
  loginType:"google",
  email:'sarith.madhu@gmail.com', 
  password : 'authenticated',
  rememberMe : 0
}

var loginResponseSuccess = {
    
    authToken: successfulAuthToken,
    isAdmin:true
    
}
var loginResponseFailure = {

    message:"MOCK : Invalid userid or password"
}
var mockLoginSuccess={
    url: loginApiUrl,
    data: function( data ) {
        return isEqualObjects( data, successfulLoginRequest ) || isEqualObjects( data, successfulLoginRequestGoogle );
      },
    status:200,
    responseText:loginResponseSuccess
  };

  var mockLoginFailure={
    url: loginApiUrl,
    data: function( data ) {
        return !(isEqualObjects( data, successfulLoginRequest ) || isEqualObjects( data, successfulLoginRequestGoogle ));
      },
    status:401,
    responseText:loginResponseFailure
  };
  
  var mockhandlers=
    [mockLoginSuccess,
     mockLoginFailure
    ];
  
