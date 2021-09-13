window.addEventListener('load', function() {
	let city = document.getElementById('id_city');
	if (city) {
		city.addEventListener('change', function(event) {
			if(event.target.value) {
				fetch(`/api/cities/${event.target.value}/`)
				.then(response => response.json())
				.then(data => {
					console.log(data);
					document.getElementById('id_service_amount').value = data.service_amount
					document.getElementById('id_employee_amount').value = data.employee_amount
					document.getElementById('id_aedo_amount').value = data.aedo_amount
				});
			}
		});
	}
});