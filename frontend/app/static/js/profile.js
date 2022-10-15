$(function () {
    $("#accordion").accordion({ heightStyle: 'panel', collapsible: true });
});

$(document).ready(function () {
    validateFormsAndAddHandlers();
    loadProfileData();


});

function updateProfile(data) {
    $('#first-name').val(data.firstName);
    $('#last-name').val(data.lastName);
}
function loadProfileData() {
    try {
        $.ajax({
            data: {
                authToken: getUserToken()
            },
            type: 'POST',
            url: getApiUrl('getProfile'),
            success: function (data) {
                //In case of success the data contains the JSON

                if (data.status == true) {
                    updateProfile(data.userData);
                }
                else {
                    showAlert('#profile-errorMessage', 'alert-warning', "Profile Update!!", data.message);

                }


            },
            error: function (data) {
                // in case of error we need to read response from data.responseJSON
                showAlert('#profile-errorMessage', 'alert-danger', "Profile Update!!", data.responseJSON.message);


            }
        }
        );
    }
    catch (e) {
        console.log(e)
    }
}


function profileUpdate() {
    try {
        $.ajax({
            data: {
                authToken: localStorage.getItem('userToken'),
                userData:
                {
                    firstName: $('#first-name').val(),
                    lastName: $('#last-name').val(),
                }

            },
            type: 'POST',
            url: getApiUrl('updateProfile'),
            success: function (data) {
                //In case of success the data contains the JSON

                if (data.status == true) {
                    showAlert('#profile-errorMessage', 'alert-success', "Profile Update!!", "Successfully updated");
                }
                else {
                    showAlert('#profile-errorMessage', 'alert-warning', "Profile Update!!", data.message);

                    //showError(data.responseJSON.message,'Profile Update')

                }


            },
            error: function (data) {
                // in case of error we need to read response from data.responseJSON
                showAlert('#profile-errorMessage', 'alert-danger', "Profile Update!!", data.responseJSON.message);

            }
        }
        );
    }
    catch (e) {
        console.log(e)
    }
}

function changePassword() {
    removeAlert('#password-errorMessage');
    try {
        $.ajax({
            data: {
                authToken: localStorage.getItem('userToken'),
                currentPassword: $('#current-password').val(),
                newPassword: $('#new-password').val(),

            },
            type: 'POST',
            url: getApiUrl('changePassword'),
            success: function (data) {
                //In case of success the data contains the JSON

                if (data.status == true) {
                    showAlert('#password-errorMessage', 'alert-success', "Change Password!!", "Successfully changed");
                }
                else {
                    showAlert('#password-errorMessage', 'alert-warning', "Change Password!!", data.message);

                    //showError(data.responseJSON.message,'Profile Update')

                }


            },
            error: function (data) {
                // in case of error we need to read response from data.responseJSON
                showAlert('#password-errorMessage', 'alert-danger', "Change Password!!", data.responseJSON.message);

            }
        }
        );
    }
    catch (e) {
        console.log(e)
    }
}
function deleteAccount()
{

}
var passwordFormRules =
{
    'current-password': {
        required: true,
    },
    'new-password': {
        required: true,
        minlength: 6
    },
    'confirm-password': {
        required: true,
        equalTo: "#new-password"
    }

};

var passwordFormMessages =
{

    'current-password': {
        required: "Cannot be blank"
    },
    'new-password': {
        required: "Cannot be blank",
        minlength: "Need at least 6 characters"
    },
    'confirm-password': {
        required: "Confirm your new password",
        equalTo: "Should be same as above"

    },

};

var profileUpdateRules =
{

    'first-name': {
        require_from_group: [1, ".form-control"]

    },
    'last-name': {
        require_from_group: [1, ".form-control"]

    }

};

var profileUpdateMessages =
{

    'first-name': {
        require_from_group: "At least one field is needed"

    },
    'last-name': {
        require_from_group: "At least one field is needed"
    }
};

var deleteAccountRules =
{

    'delete-password': {
        required:true

    },
    'confirm-delete': {
        required:true

    }

};

var deleteAccountMessages =
{

    'delete-password': {
       required: "Confirm your password"

    },
    'confirm-delete': {
       required: "Please check the box"
    }
};
function validateFormsAndAddHandlers() {

    $("#password").validate({
        rules: passwordFormRules,
        errorClass: "inputValidationError",

        submitHandler: function (form) {
            changePassword();
        },
        messages: passwordFormMessages
    });

    $("#profileForm").validate({
        rules: profileUpdateRules,
        errorClass: "inputValidationError",

        submitHandler: function (form) {
            profileUpdate();
        },
        messages: profileUpdateMessages
    }

    );

    $("#deleteAccount").validate({
        rules: deleteAccountRules,
        errorClass: "inputValidationError",

        submitHandler: function (form) {
            deleteAccount();
        },
        messages: deleteAccountMessages
    }

    );
    $("form").each(function () {
        $(this).validate();
    });

}