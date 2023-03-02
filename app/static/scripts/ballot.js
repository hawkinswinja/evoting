$(document).ready(function() {
  $('#results').on('click', () => { window.location = "/e-portal"; });

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
			  dataType: 'text',
			  data: formData, 
			  success: function(data) {
				  if (data == 'voted') { 
					  alert('Cannot vote again for this position'); } else {
						  alert('You successfully voted for ' + name); }
				 },
			  error: function(xhr, status, error){
				  alert('Error submitting form ' + error);
				 }
			});
	      $('#ballot_form')[0].reset();
	  }
  });

});
