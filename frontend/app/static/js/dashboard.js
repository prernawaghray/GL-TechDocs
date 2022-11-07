
$(document).ready(function () {
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
}});
function getfilelist() {
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
                  if(len > 0){
                    txt += 
                              '<thead><tr><th><input type="checkbox" id="selectall"></th><th scope="col">Title</th><th scope="col">Version</th><th scope="col">Last Modified</th>'+
                              '<th scope="col">Modified By</th><th scope="col">Actions</th></tr></thead><tbody></tbody>'
                      for(var i=0;i<len;i++){
                        var documentURL = getFrontEndUrl('latex-editor/'+data.Documents[i].DocId);
                  
                          if(data.Documents[i].DocName || data.Documents[i].Version || data.Documents[i].LastModifiedOn || data.Documents[i].LastModifiedBy){
                              txt+=                              
                              '<tr><td><input type="checkbox" class="case">'+"</td><td>"+
                              '<a href=\''+documentURL+' \'">'+data.Documents[i].DocName+'</a>'+"</td><td>"+
                              data.Documents[i].Version+ 
                              "</td><td>"+data.Documents[i].LastModifiedOn+"</td><td>"+data.Documents[i].LastModifiedBy + "</td>" +
                              '<td><div class="btn-group" role="group" aria-label="ROW BTNS">' +
                              
                              '<button type="button" id="rename" onclick="renamedata()" style="height: 25px; width: 25px; padding: 0px;" title="Rename"' +
                                'data-bs-toggle="modal" data-bs-target="#renameModal" class="btn btn-outline-dark">' +
                                '<i class="bi bi-input-cursor-text" style="font-size: 16px;"></i>' +
                              '</button>' +

                              '<button type="button" style="height: 25px; width: 25px; padding: 0px;" title="Share" data-docid="2" data-bs-toggle="modal"' + 
                              'data-bs-target="#shareModal" title="Share" class="btn btn-outline-dark">' + 
                              '<i class="bi bi-share" style="font-size: 16px;"></i>' +
                              '</button>' +

                              '<button type="button" id="download" style="height: 25px; width: 25px; padding: 0px;" title="Download"' +
                                'class="btn btn-outline-dark">' +
                                '<i class="bi bi-download" style="font-size: 16px;"></i>' +
                              '</button>' +

                              '<button type="button" id="archive" style="height: 25px; width: 25px; padding: 0px;" title="Archive"' +
                                'class="btn btn-outline-dark">' +
                                '<i class="bi bi-file-earmark-zip" style="font-size: 16px;"></i>' +
                              '</button>' +

                              '<button type="button" id="delete" onclick="openmodal('+data.Documents[i].DocId+')" style="height: 25px; width: 25px; padding: 0px;" title="Move to Trash"' +
                              ' class="btn btn-outline-dark">' +
                                '<i class="bi bi-trash3" style="font-size: 16px;"></i>' +
                              '</button>' +
                              
                            
                              "</div></td></tr>";
                          }
                      }
                      if(txt != ""){
                          $("#table1").html(txt).removeClass("hidden");
                          
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

window.onload = getfilelist();

// Rename file
function renamefile() {
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
}

//Move to trash

function deletedata(DocId) {
  try {
    $.ajax({
       // headers: {'authToken': getUserToken(),},
        contentType:"application/json; charset=utf-8",
        dataType: "json",
        data: JSON.stringify({
            DocId: DocId
        }),
        type: 'POST',
        url: getApiUrl('filetrash'),
        success: function (data) {
          alert("File moved to trash");
          getfilelist();
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
};

function openmodal(DocId) {
  let text;
  if (confirm("Do you want to delete this file?") == true) {
    deletedata(DocId);
  } else {
    
  }
}
          
//Get Trash List
function trashlist() {
  try {
    $.ajax({
        headers: {'authToken': getUserToken()},
        type: 'GET',
        url: getApiUrl('getTrashList'),
        success: function(data){
          t1 = document.getElementById('table1');
          t2 = document.getElementById('table2');
          b1 = document.getElementById('new-doc');
          b2 = document.getElementById('share-doc');
          b3 = document.getElementById('archive-doc');
          b4 = document.getElementById('trash-doc');
          
          t1.style.display='none';
          b1.style.display='none';
          b2.style.display='none';
          b3.style.display='none';
          b4.style.display='none';
          $("#multi-retrieve").removeClass("hidden");
          $("#multi-delete").removeClass("hidden");

          if(data){
            var len = Object.keys(data.Documents).length;
            var txt = "";
            
            if(len > 0){
              txt += 
                        '<thead><tr><th><input type="checkbox" id="selectalltrash"></th><th>Title</th><th>Actions</th></tr></thead><tbody></tbody>'
                for(var i=0;i<len;i++){
            
                    if(data.Documents[i].DocName){
                      
                        txt+=                              
                        '<tr><td><input type="checkbox" class="casetrash">'+"</td><td>"+data.Documents[i].DocName + "</td>"+
                        '<td><div class="btn-group" role="group" aria-label="ROW BTNS">' +
                        '<button type="button" id="retrieve" style="height: 25px; width: 25px; padding: 0px;" title="Retrieve"' +
                          'class="btn btn-outline-dark">' +
                          '<i class="bi bi-arrow-90deg-right" style="font-size: 16px;"></i>' +
                        '</button>' +

                        '<button type="button" id="delete" style="height: 25px; width: 25px; padding: 0px;" title="Delete permanently"' +
                          'data-bs-toggle="modal" data-bs-target="#delModal" class="btn btn-outline-dark">' +
                          '<i class="bi bi-x-circle" style="font-size: 16px;"></i>' +
                        '</button>' +
                      
                        "</div></td></tr>";
                    }
                }
                if(txt != ""){
                    $("#table2").html(txt).removeClass("hidden");
                    
                    // Add multiple select / deselect functionality
                    $("#selectalltrash").click(function () {
                      $('.casetrash').attr('checked', this.checked);
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