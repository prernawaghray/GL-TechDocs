var rootApiUrl = "http://localhost:56733/api/";
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

