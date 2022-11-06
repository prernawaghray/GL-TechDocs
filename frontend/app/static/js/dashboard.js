const links = document.querySelectorAll('.nav-link');
    
if (links.length) {
  links.forEach((link) => {
    link.addEventListener('click', (e) => {
      links.forEach((link) => {
          link.classList.remove('active');
      });
      e.preventDefault();
      link.classList.add('active');
    });
  });
}
$(document).ready( function() {
  $('table tr').click( function getdocid() {
      index = $(this).index();
      doc_id = data.Documents[index].DocId;
      return doc_id;
  }); 
});

$(document).ready(function () {
  
window.onload = function getfilelist() {
  
    try {
        $.ajax({
            headers: {'authToken': getUserToken()},
            type: 'GET',
            url: getApiUrl('filegetlist'),
            success: function(data){
              doc_data = JSON.stringify(data); 
              if(data){
                  var len = Object.keys(data.Documents).length;
                  var txt = "";
                  //getdocid();
                  if(len > 0){
                      for(var i=0;i<len;i++){
                        var documentURL = getFrontEndUrl('latex-editor/'+data.Documents[i].DocId);
                  
                          if(data.Documents[i].DocName || data.Documents[i].Version || data.Documents[i].LastModifiedOn || data.Documents[i].LastModifiedBy){
                              txt += '<tr><td><input type="checkbox" class="case">'+"</td><td>"+
                              '<a class="input" onclick="window.location.href=\''+documentURL+' \'">'+data.Documents[i].DocName+'</a>'+"</td><td>"+
                              data.Documents[i].Version+ 
                              "</td><td>"+data.Documents[i].LastModifiedOn+"</td><td>"+data.Documents[i].LastModifiedBy + "</td>" +
                              '<td>' +
                              '<button type="button" id="rename" onclick="renamedata()" style="height: 25px; width: 25px; padding: 0px;" title="Rename" data-docid="2"' +
                                'data-bs-toggle="modal" data-bs-target="#renameModal" class="btn btn-outline-dark">' +
                                '<i class="bi bi-input-cursor-text" style="font-size: 16px;"></i>' +
                              '</button>' +

                              '<button type="button" style="height: 25px; width: 25px; padding: 0px;" title="Share" data-docid="2" data-bs-toggle="modal"' + 
                              'data-bs-target="#shareModal" title="Share" class="btn btn-outline-dark">' + 
                              '<i class="bi bi-share" style="font-size: 16px;"></i>' +
                              '</button>' +

                              '<button type="button" style="height: 25px; width: 25px; padding: 0px;" title="Download"' +
                                'class="btn btn-outline-dark">' +
                                '<i class="bi bi-download" style="font-size: 16px;"></i>' +
                              '</button>' +

                              '<button type="button" id="delete" onclick="deletedata()" style="height: 25px; width: 25px; padding: 0px;" title="Move to Trash" data-docid="2"' +
                                'data-bs-toggle="modal" data-bs-target="#delModal" class="btn btn-outline-dark">' +
                                '<i class="bi bi-trash3" style="font-size: 16px;"></i>' +
                              '</button>' +
                            
                              "</td></tr>";
                          }
                      }
                      if(txt != ""){
                          $("#tbody").append(txt).removeClass("hidden");
                          
                          // Add multiple select / deselect functionality
                          $("#selectall").click(function () {
                            $('.case').attr('checked', this.checked);
                              })
                          
                      }
                  }
              }
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

// Search functionality
function filterTable(event) {
  let filter = event.target.value.trim().toLowerCase();
  let rows = document.querySelector('#table tbody').rows;
  for (let i = 0; i < rows.length; i++) {
    let row = rows[i], show = false;
    if (filter.length > 0) {
      for (let j = 0; j < row.children.length; j++) {
        let col = row.children[j], text = col.textContent.toLowerCase();
        if (text.indexOf(filter) > -1) {
          show = true;
          continue;
        }
      }
    } else {
      show = true;
    }
    toggleClass(row, 'hidden-row', !show);
  }
}

function toggleClass(el, className, state) {
  if (el.classList) el.classList.toggle(className, state);
  else {
    var classes = el.className.split(' ');
    var existingIndex = classes.indexOf(className);
    if (state === undefined) {
      if (existingIndex > -1) classes.splice(existingIndex, 1)
      else classes.push(existingIndex);
    } else {
      if (!state) classes.splice(existingIndex, 1)
      else classes.push(existingIndex);
    }
    el.className = classes.join(' ');
  }
}

document.querySelector('#search').addEventListener('keyup', filterTable, false);
})

// Rename file
$("#renamefile").click(function renamefile() {
  
  try {
      $.ajax({
          headers: {'authToken': getUserToken()},
          data: {
            DocId: doc_id,
            DocName: $('#name').val()
          },
          type: 'POST',
          url: getApiUrl('filerename'),
          success: function (data) {
            alert(data);
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
})

//Move to trash

$("#delete").click(function trashfile() {
 
  try {
    $.ajax({
        headers: {'authToken': getUserToken()},
        data: {
          DocId: doc_id
        },
        type: 'POST',
        url: getApiUrl('filetrash'),
        success: function (data) {
          alert("File moved to trash");
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
})
          
//Get Trash List
$('#trashed').click( function trashlist() {
  try {
    $.ajax({
        headers: {'authToken': getUserToken()},
        type: 'GET',
        url: getApiUrl('getTrashList'),
        success: function(data){

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
})