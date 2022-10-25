var rootApiUrl = "http://localhost:56733/api/";
//56733
//6622
var rootFrontEndUrl = "http://localhost:56733/";
function getApiUrl(api)
{
    return rootApiUrl+api;
}
function getFrontEndUrl(path)
{
    return rootFrontEndUrl+path;
}

function getUserToken()
{
    try
    {
        authToken = localStorage.getItem('userToken');
        if(authToken)
            return authToken;
        else
            window.location.replace('/login');
    }
    catch(e)
    {
        console.log(e)
        window.location.replace('/login')
    }
}

function parseJwt (token) {
    var base64Url = token.split('.')[1];
    var base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
    var jsonPayload = decodeURIComponent(window.atob(base64).split('').map(function(c) {
        return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
    }).join(''));

    return JSON.parse(jsonPayload);
};

function getResponseMessage(data)
{
    if("responseJSON" in data && data.responseJSON !=undefined)
      if("message" in data.responseJSON)
        return data.responseJSON.message;
    
        return data.statusText;
}

function getLoginType()
{
    parsedToken=parseJwt(getUserToken());
    if(parsedToken.loginType!=undefined)
        return parsedToken.loginType;
    else
        return "email";

}
