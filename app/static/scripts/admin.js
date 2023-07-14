$(document).ready(function() {
  $('#results').on('click', () => { window.location.replace = "/e-portal"; });

  $('#search').on('click', function() {
      const url = '/candidates/' + $('#filterpost').val();
	  fetch(url)
	  .then(response => response.json())
	  .then(data => {
		$('#all li').remove();
		const list = document.getElementById('all');
		for (const key in data) {
			let li = document.createElement('li');
			li.innerText = key + '  ' + data[key].name + '  ' + data[key].post;
			list.appendChild(li);
		}
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
