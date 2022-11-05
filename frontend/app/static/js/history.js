
$(document).ready(function() {
	console.log("ready")
    $('#historyClick').on('click', function(event) {
        console.log("Load History")
        $('#historyDetailsDiv').html('Loading ....');
        let jsonHistory = {"items": [{"datetime":"60 mins ago", "desc": "John edited an item.", "operation":"Filename.ext"},{"datetime":"20 mins ago", "desc": "Johnny edited an item.", "operation":"SomeFilename.ext"},{"datetime":"10 mins ago", "desc": "Mary edited an item.", "operation":"OldFilename.ext"}]}

        let history = '';
        	$.each(jsonHistory.items, function (key, value) { 
        		history += '<table class="table table-hover"><thead><tr><th>'+value.datetime+'</th></tr></thead><tbody>';
      			history += '<tr><td>'+value.desc+'</td></tr><tr><td><a href="#">'+value.operation+'</a></td></tr></tbody></table>';
        	});
      		
        $('#historyDetailsDiv').html(history);
     });
});