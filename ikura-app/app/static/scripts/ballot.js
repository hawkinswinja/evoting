$(document).ready(function () {

	// Get the modal
	let modal = $("#positionsModal");

	// Get the button that opens the modal
	const btn = $("#positionsBtn");

	// Get the <span> element that closes the modal
	const span = $(".close");

	// When the user clicks the button, open the modal
	btn.on('click', function() {
		const myid = btn.data('myid');
		$.ajax({
			url: '/posts',
			method: 'GET',
			success: function(data) {
				var positionsList = '';
				data.forEach(function(position) {
					positionsList += '<li><a href="/vote/' + myid + '/' + position + '">' + position + '</a></li>';
				});
				positionsList += '<li><a href="/selection/' + myid + '">mychoice</a></li>';
				console.log(positionsList);
				modal.find('ul').html(positionsList);
				modal.css("display", "block");
			},
			error: function(error) {
				console.log("Error fetching positions:", error);
			}
		});
	});

	// When the user clicks on <span> (x), close the modal
	span.on('click', function() {
		// modal.css("width", "0");
		modal.css("display", "none");
	});

	// When the user clicks anywhere outside of the modal, close it
	$(window).on('click', function(event) {
		if ($(event.target).is(modal)) {
			modal.css("display", "none");
		}
	});


	$('#results').on('click', () => { window.location = "/e-portal"; });

	$('.exit').on('click', () => { window.location = "/logout"; });

	$('.vote').on('click', () => {
		message = 'This action changes your vote status and you will no longer be able to make vote changes'
		const confirmation = confirm(message)

		if (confirmation) {
			$.ajax({
				url: '/vote',
				dataType: 'text',
				success: function (data) {
					alert(data);
				},
				error: function (error) {
					alert('Error submitting form ');
				},
				complete: () => {
					window.location = '/logout';
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
