/*
* This function collect all the existing reservations and put it in the calendar
*
*/
function initializeCalendar () {
  var events = [];
  var colors = ['blue','red','orange','green','pink','black'];
  $.ajax({
    url: '/reservations',
    dataType: 'json',
    success: function (data) {
      data.forEach(function(reservation){
        // We look if the id_room < colors.size
        if (reservation.room < colors.length){
          events.push({title: reservation.reason, start: reservation.startTime.split('Z')[0],
          end: reservation.endTime.split('Z')[0], allDay: false, color: colors[reservation.room-1]});
        } else {
          events.push({title: reservation.reason, start: reservation.startTime.split('Z')[0],
          end: reservation.endTime.split('Z')[0], allDay: false});
        }

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

initializeCalendar();
