$(document).ready(function() {

  $('button[name="results"]').on('click', function() {
      const url = '/candidates/' + $('#filterpost').val();
	  fetch(url)
	  .then(response => response.json())
	  .then(data => {
		$('#candidates li').remove();
		const list = document.getElementById('candidates');
		for (const key in data) {
			let li = document.createElement('li');
			li.innerText = data[key].name + '  ' + data[key].post + ' ' + data[key].votes;
			list.appendChild(li);
		}
	  })	  
	  .catch(error => alert(error));
  });


  $('.exit').on('click', () => { window.location = "/login"; });

});
