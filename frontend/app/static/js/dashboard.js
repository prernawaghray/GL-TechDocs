function getfirstname(data) {
  userData = data.userData;
  usageStats = data.usageStats;
  firstName = userData.firstName;
  document.getElementsByClassName('page-header').innerHTML = header;
}

function getusername() {
  try {
      $.ajax({
          data: {
              user_id: getUserToken()
          },
          type: 'POST',
          url: getApiUrl('getProfile'),
          success: function (data) {
              //In case of success the data contains the JSON

                  getfirstname(data);

          },
      });
  }
  catch (err) {
      console.log(err)
  }
}

function pageHeader() {
  let header = '';
  header += 'Welcome' + firstName + '!';
}


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
                '<button type="button" id="edit" style="height: 25px; width: 25px; padding: 0px;" title="Edit"' +
                  'class="btn btn-outline-dark"' +
                  'onclick="window.location.href="{{url_for("latexEditor",id="edit-document")}}"">' +
                  '<i class="bi bi-pencil-square"></i>' +
                '</button>' +

                '<button type="button" style="height: 25px; width: 25px; padding: 0px;" title="Share" data-docid="2"' +
                  'data-bs-toggle="modal" data-bs-target="#shareModal" class="btn btn-outline-dark">' +
                  '<i class="bi bi-share" style="font-size: 16px;"></i>' +
                '</button>' +

                '<button type="button" id="rename" onclick="renamedata()" style="height: 25px; width: 25px; padding: 0px;" title="Rename" data-docid="4"' +
                  'data-bs-toggle="modal" data-bs-target="#renameModal" class="btn btn-outline-dark">' +
                  '<i class="bi bi-input-cursor-text" style="font-size: 16px;"></i>' +
                '</button>' +

                '<button type="button" style="height: 25px; width: 25px; padding: 0px;" title="Download"' +
                  'class="btn btn-outline-dark">' +
                  '<i class="bi bi-download" style="font-size: 16px;"></i>' +
                '</button>' +

                '<button type="button" id="delete" onclick="deletedata()" style="height: 25px; width: 25px; padding: 0px;" title="Delete" data-docid="2"' +
                  'data-bs-toggle="modal" data-bs-target="#delmodal" class="btn btn-outline-dark">' +
                  '<i class="bi bi-trash3" style="font-size: 16px;"></i>' +
                '</button>' +
              '</td>';

            doc += '</tr>';
        };
        
function fileSearch() {
  let input = document.getElementById("searchbar").value
  input = input.toLowerCase();
  let x = document.getElementsByClassName("DocName");

  for (i=0; i<x.length; i++) {
    if (!x[i].innerHTML.toLowerCase().includes(input)) {
      x[i].style.display = 'none';
    }
    else {
      x[i].style.display = 'table-cell'
    }
  }
};

function renamedata() {
  renameData = {
    user_id : getUserToken(),
    doc_id : json_str[$("#tbody").$(this).index()].DocId,
    doc_name: $('#renameFile').val(),
        };
renamefile(renameData);
}

function renamefile(renameData) {
  try {
      $.ajax({
          data: renameData,
          type: 'POST',
          url: getApiUrl('file_Rename'),
          success: function (data) {
          },
          error: function (data) {
              // in case of error we need to read response from data.responseJSON
              showAlert('#rename-error-message', 'alert-danger', "", getResponseMessage(data));
          }
      });
  }
  catch (err) {
      console.log(err)
  }
}

function deletedata() {
  deleteData = {
    user_id : getUserToken(),
    doc_id : json_str[$("#tbody").$(this).index()].DocId,
        };
deletefile(deleteData);
}

function deletefile(deleteData) {
  try {
    $.ajax({
        data: renameData,
        type: 'POST',
        url: getApiUrl('file_delete'),
        success: function (data) {
        },
        error: function (data) {
            // in case of error we need to read response from data.responseJSON
            showAlert('#delete-error-message', 'alert-danger', "", getResponseMessage(data));
        }
    });
}
catch (err) {
    console.log(err)
}
}

// File Upload
document.querySelector('.custom-file-input').addEventListener('change', function (e) {
var name = document.getElementById("customFileInput").files[0].name;
var nextSibling = e.target.nextElementSibling
nextSibling.innerText = name
})


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