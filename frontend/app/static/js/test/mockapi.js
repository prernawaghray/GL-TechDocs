// Helper function
import { mockhandlers as loginhandlers } from "./mocks/mocklogin.js"
import { mockhandlers as profilehandlers } from "./mocks/mockprofile.js";
import { mockhandlers as deletehandlers } from "./mocks/mockDeleteAccount.js";
var mockhandlers = [];
mockhandlers.push(...loginhandlers,...profilehandlers,...deletehandlers);

var mockjaxhandlers = $.mockjax(
    mockhandlers
);