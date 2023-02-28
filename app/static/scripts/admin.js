$(document).ready(function() {
  $('#search').on('click', function() {
      const url = '/candidates/' + $('#filterpost').val();
	  fetch(url)
	  .then(response => response.json())
	  .then(data => {
		$('#candidates li').remove();
		let list = document.getElementById('candidates')
		data.forEach((user) => {
			let li = document.createElement('li');
			li.innerText = user.id + '  ' + user.name + '  ' + user.post;
			list.appendChild(li);
		});
	  })	  
	  .catch(error => alert(error));
  });

  $('button[name="clearposts"]').on('click', function() {
	  fetch('/clear/posts')
	  .then(response => {
		  if (response.status == 200) { 
			  alert('Succcesful'); 
			  window.location.reload();}
	  })
	  .catch(error => alert(error));
	});
  $('button[name="clearcands"]').on('click', function() {
	  fetch('/clear/candidates')
	  .then(response => {
		  if (response.status == 200) { 
			  alert('Succcesful'); 
			  window.location.reload();}
	  })
	  .catch(error => alert(error));
	});
  $('.exit').on('click', () => { window.location = "/login"; });
});
