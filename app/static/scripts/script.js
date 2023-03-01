$(document).ready(function() {
  $('#search').on('click', function() {
      const url = '/candidates/' + $('#filterpost').val();
	  fetch(url)
	  .then(response => response.json())
	  .then(data => {
		$('#candidates li').remove();
		const list = document.getElementById('candidates');
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
  
  $('#ballot_form').submit(function(event) {
	  event.preventDefault(); //prevent the form from submitting
	  const formData = $(this).serialize();
	  const id = $('input[type="radio"]:checked').val();
	  const name = $('input[type="radio"]:checked').closest('label').find('span').text();

	  const confirmation = confirm('Confirm selected candidate\n id:' + id +'\nName: ' + name);

	  if (confirmation) {
		  $.ajax({
			  url: $(this).attr('action'), 
			  type: $(this).attr('method'),
			  data: formData, 
			  success: function(response) {
	              $('#ballot_form')[0].reset();
				  alert('You successfully voted for ' + name);
				 },
			  error: function(xhr, status, error){
				  alert('Error submitting form' + error);
				 }
			});
	  }
  });

});
