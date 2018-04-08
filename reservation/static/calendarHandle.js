/*
* This function collect all the existing reservations and put it in the calendar
*
*/
function getEventsFromDb () {
  var events = [];
  $.ajax({
    url: '/reservations',
    dataType: 'json',
    success: function (data) {
      data.forEach(function(reservation){
        events.push({title: reservation.reason, start: reservation.startTime.split('Z')[0], end: reservation.endTime.split('Z')[0], allDay: false});
      })


      $('#calendar').fullCalendar({
        defaultView: 'agendaWeek',
        events: events
      })
    },
    error: function (err) {
      console.log("Error :",err);
    }
  })
}

getEventsFromDb();
