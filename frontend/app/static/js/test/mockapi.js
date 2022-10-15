// Helper function
import { mockhandlers as loginhandlers } from "./mocks/mocklogin.js"
import { mockhandlers as profilehandlers } from "./mocks/mockprofile.js";

var mockhandlers = [];
mockhandlers.push(...loginhandlers,...profilehandlers);

var mockjaxhandlers = $.mockjax(
    mockhandlers
);