// We handle the csrf token to use AJAX
var csrftoken = Cookies.get('csrftoken');
function csrfSafeMethod(method) {
  // these HTTP methods do not require CSRF protection
  return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
  beforeSend: function(xhr, settings) {
      if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
          xhr.setRequestHeader("X-CSRFToken", csrftoken);
      }
  }
});

// We send the DELETE request with AJAX
$('.btn').on('click', function () {
  $.ajax({
      type: 'DELETE',
      url: '/reservations/' + $(this).attr('idResa') + '/',
      success: function() {
        sendMessage("New reservation");
        window.location.replace("/myreservation");
      },
      error: function (err) {
        console.log("Error: ",err);
      }
  })
})
