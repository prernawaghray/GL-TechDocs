
function saveUsertoLocal (userObject){

		localStorage.setItem(userObject, []);
		return true;

	}

	function deleteUserInLocal (userObject){

		localStorage.removeItem(userObject);
		return true;
	}
	
	function newDocumentInLocal(documentObject){
		
		localStorage.setItem(documentObject.local_key,documentObject.document);
		return true;}


	function updateDocumentInLocal (documentObject){
		localStorage.setItem(documentObject.local_key,localStorage.getItem(documentObject.local_key).push(documentObject.document)); 

		return true;
	}

