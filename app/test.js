$('button[name="search"]').on('click', function() {
	fetch('localhost:5000/posts')
	.then(response => response.json())
	.then(data => alert(data))
	.catch(error => alert(error));
});
