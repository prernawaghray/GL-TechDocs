
function updatefilelist(data) {
    userid = data.userid;
    json_str = data.json_str;
}


function getfilelist() {
    try {
        $.ajax({
            data: {
                user_id: getUserToken()
            },
            type: 'GET',
            url: getApiUrl('file_GetList'),
            success: function (data) {
                //In case of success the data contains the JSON

                    updatefilelist(data);
 
            },
            error: function (data) {
                // in case of error we need to read response from data.responseJSON
                showAlert('#filelist-error-message', 'alert-danger', "", getResponseMessage(data));
            }
        });
    }
    catch (err) {
        console.log(err)
    }
}

  
// FETCHING DATA FROM JSON
        var doc = '';

        // ITERATING THROUGH OBJECTS
        json_str.forEach(file_List);
        document.getElementById("tbody").innerHTML = doc;
            //CONSTRUCTION OF ROWS HAVING
            // DATA FROM JSON OBJECT
        function file_List(value, key) {
            doc += '<tr>';
            doc += '<td>'+
                '<input type="checkbox" class="case">' +
                '</td>';
            doc += '<td scope="col">' + 
                value.DocName + '</td>';

            doc += '<td scope="col">' + 
                value.Version + '</td>';

            doc += '<td scope="col">' + 
                value.LastModifiedOn + '</td>';

            doc += '<td scope="col">' + 
                value.LastModifiedBy + '</td>';

            doc += '<td>' + 
                '<button type="button" style="height: 25px; width: 25px; padding: 0px;" title="Share" data-docid="2"' +
                  'data-bs-toggle="modal" data-bs-target="#shareModal" class="btn btn-outline-dark">' +
                  '<i class="bi bi-share" style="font-size: 16px;"></i>' +
                '</button>' +

                '<button type="button" style="height: 25px; width: 25px; padding: 0px;" title="Copy"' +
                  'class="btn btn-outline-dark">' +
                  '<i class="bi bi-files" style="font-size: 16px;"></i>' +
                '</button>' +

                '<button type="button" style="height: 25px; width: 25px; padding: 0px;" title="Archive"' +
                  'class="btn btn-outline-dark disabled">' +
                  '<i class="bi bi-file-earmark-zip" style="font-size: 16px;"></i>' +
                '</button>' +

                '<button type="button" style="height: 25px; width: 25px; padding: 0px;" title="Download"' +
                  'class="btn btn-outline-dark">' +
                  '<i class="bi bi-download" style="font-size: 16px;"></i>' +
                '</button>' +

                '<button type="button" style="height: 25px; width: 25px; padding: 0px;" title="Delete" data-docid="2"' +
                  'data-bs-toggle="modal" data-bs-target="#delmodal" class="btn btn-outline-dark">' +
                  '<i class="bi bi-trash3" style="font-size: 16px;"></i>' +
                '</button>' +
              '</td>';

            doc += '</tr>';
        };
        


// Add multiple select / deselect functionality
$(document).ready(function () {
    $("#selectall").click(function () {
    $('.case').attr('checked', this.checked);
      });
          
// If all checkboxes are selected, check the selectall checkbox also        
$(".case").click(function () {
if ($(".case").length == $(".case:checked").length) {
    $("#selectall").attr("checked", "checked");
    }
else {
    $("#selectall").removeAttr("checked");
    }
  });
  });



/* var rowCount = $("#myTable tr").length - 1;
if (rowCount <= 0) {
  $('#selectall').attr('disabled', true);
}
else {

  $('#selectall').attr('disabled', false);
} */