$('[type="submit"]').on('click', function(event){

  var form = {"csrfmiddlewaretoken": $('[name="csrfmiddlewaretoken"]').val(),
    "reason": $('#id_reason').val(),
    "startTime": $('#id_startTime').val(),
    "endTime": $('#id_endTime').val(),
    "room": $('#id_room').val(),
    "owner": $('#username').attr('username')
  };

  event.preventDefault();
  $.ajax({
    url: '/reservations/',
    method: 'post',
    dataType: 'json',
    data: form,
    success: function(data){
      console.log("Success :",data);
      sendMessage("New reservation");
      window.location.replace('/');
    },
    error: function (err) {console.log("Error :",err);}
  })
})
