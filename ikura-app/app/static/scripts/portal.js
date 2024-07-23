$(document).ready(function() {

	$('button[name="results"]').on('click', function() {
		const url = '/candidates/' + $('#filterpost').val();
		fetch(url)
		.then(response => response.json())
		.then(data => {
		  $('#candidates').empty(); // Clear existing list items
		  const list = document.getElementById('candidates');
		  const header = document.createElement('h3');
		  header.innerHTML = "Name&emsp;Position&ensp;Votes";
		  list.appendChild(header);
		  for (const cand of Object.values(data)) {
			  const li = document.createElement('li');
			  li.innerHTML = cand.name + '&emsp;' + cand.post + '&emsp;' + cand.votes;
			  list.appendChild(li);
		  }
		})	  
		.catch(error => alert(error));
	});
  
	$('.exit').on('click', () => { window.location = "/logout"; });
  
  });
  