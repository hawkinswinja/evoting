$(document).ready(function() {

  $('button[name="results"]').on('click', function() {
      const url = '/candidates/' + $('#filterpost').val();
	  fetch(url)
	  .then(response => response.json())
	  .then(data => {
		$('#candidates li').empty();
		const list = document.getElementById('candidates');
		// list.html("<h3>Name&emsp;Position&ensp;Votes</h3>")
		for (const cand of Object.values(data)) {
			const li = document.createElement('li');
			li.innerHTML = cand.name + '&emsp;' + cand.post + '&emsp;' + cand.votes;
			list.appendChild(li);
		}
	  })	  
	  .catch(error => alert(error));
  });


  $('.exit').on('click', () => { window.location = "/login"; });

});
