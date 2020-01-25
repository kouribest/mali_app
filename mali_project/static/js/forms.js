function getCookie(name) {
	var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function toggleClass(initial, current){
	$('.'+initial+'_block').fadeOut(function(){
		$(this).hide()
		$('.'+current +'_block').fadeIn(function(){
			$(this).show()
		})
	})	
}

$('document').ready(function(){

	toastr.options = {
	  "closeButton": true,
	  "debug": false,
	  "newestOnTop": false,
	  "progressBar": false,
	  "positionClass": "toast-bottom-full-width",
	  "preventDuplicates": false,
	  "onclick": null,
	  "showDuration": "300",
	  "hideDuration": "1000",
	  "timeOut": "10000",
	  "extendedTimeOut": "1000",
	  "showEasing": "swing",
	  "hideEasing": "linear",
	  "showMethod": "fadeIn",
	  "hideMethod": "fadeOut",
	}
	var tmp= $('#id_type_voyage').val()
	$('#id_type_voyage').on('change', function(){
		current_value= $(this).val()
		toggleClass(tmp, current_value)
		tmp= current_value
	})

	$('.ui.form').form({
		onSuccess: function(event, fields){
			event.preventDefault();

			data= $('form').serialize();
			$.ajaxSetup({headers: {"X-CSRFToken": getCookie('csrftoken')}});
			$.ajax({
				url:'/addform',
				dataType:'json',
				type: 'POST',
				data: data,
				success: function(res){
					$('.ui.card > .image').html(res.path)
					$('.ui.basic.modal').modal('show')
				},
				error: function(msg){
					error= JSON.parse(msg.responseText)
					toastr.error('Votre formulaire est invalide', error['error'])
				}
			})
		}
	})
})