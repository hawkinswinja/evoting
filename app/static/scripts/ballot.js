$(document).ready(function () {
	$('#results').on('click', () => { window.location = "/e-portal"; });

	$('.exit').on('click', () => { window.location = "/logout"; });

	$('.vote').on('click', () => {
		message = 'This action changes your vote status to "voted"\
and you will no longer be able to make vote changes'
		const confirmation = confirm(message)

		if (confirmation) {
			$.ajax({
				url: '/vote',
				//type: '',
				dataType: 'text',
				//data: formData, 
				success: function (data) {
					alert(data);
					window.location = '/logout';
				},
				error: function (xhr, status, error) {
					alert('Error submitting form ' + error);
				}
			});
		}
	});

	const post = $('#position').val();

	$('#ballot_form').submit(function (event) {
		event.preventDefault(); //prevent the form from submitting
		const formData = $(this).serialize();
		const id = $('input[type="radio"]:checked').val();
		const name = $('input[type="radio"]:checked').closest('label').find('span').text();
		
		if (name) {
			const confirmation = confirm('Confirm selected candidate\n id:' + id + '\nName: ' + name);

			if (confirmation) {
				$.ajax({
					url: $(this).attr('action'),
					type: $(this).attr('method'),
					dataType: 'text',
					data: post + " " + String(id) + " " + name,
					success: function (data) {
						alert(data);
					},
					error: function (xhr, status, error) {
						alert('Error submitting form ' + error);
					}
				});
				$('#ballot_form')[0].reset();
			}

		} else {
			alert("Kindly make a selection before clicking the submit button")
		}

	});

});
