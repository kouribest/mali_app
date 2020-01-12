
let scanner = new Instascan.Scanner({ video: document.getElementById('qrcode_scanner') });
		scanner.addListener('scan', function (content) {
			//redirect to the update page
			window.location.href = window.location.href+'update_registration/'+content
		});
$('#scan_button').on('click', function(){
		Instascan.Camera.getCameras().then(function(cameras) {
			if (cameras.length > 0) {
				scanner.start(cameras[0]);
			} else {
				toastr.error('No cameras found.');
			}
		}).catch(function (e) {
			toastr.error(e);
		});
})