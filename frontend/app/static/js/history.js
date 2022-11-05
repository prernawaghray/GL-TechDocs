
$(document).ready(function() {
	console.log("ready")
    $('#historyClick').on('click', function(event) {
      try {
        var getHistroyData={"Email":localStorage.getItem('email'), "PageNumber": 0 };
        console.log("Getting history for :", getHistroyData)
        $.ajax({
               data : JSON.stringify(getHistroyData),
               contentType:"application/json; charset=utf-8",
               dataType: "json",
               type : 'POST',
               url : getApiUrl('history/get'),
               headers: {"Authorization": localStorage.getItem('userToken')},
               success: function(data) {
                //In case of success the data contains the JSON
                console.log("History data !!", data)
                $('#historyDetailsDiv').html('Loading ....');
                //let jsonHistory = {"items": [{"datetime":"60 mins ago", "desc": "John edited an item.", "operation":"Filename.ext"},{"datetime":"20 mins ago", "desc": "Johnny edited an item.", "operation":"SomeFilename.ext"},{"datetime":"10 mins ago", "desc": "Mary edited an item.", "operation":"OldFilename.ext"}]}
                let history = '';
                  $.each(data.items, function (key, value) { 
                    history += '<table class="table table-hover"><thead><tr><th>'+value.time+'</th></tr></thead><tbody>';
                    history += '<tr><td>'+value.action+'</td></tr><tr><td><a href="#">'+value.doc_name+'</a></td></tr></tbody></table>';
                  });
                  
                $('#historyDetailsDiv').html(history);
              },
              error:function(data) {
                // in case of error we need to read response from data.responseJSON
              
                console.log("History error data !!", data)
                $('#historyDetailsDiv').html(data);
                
              }
            });
        } catch(e) {
            console.log(e)
        }
     });
});