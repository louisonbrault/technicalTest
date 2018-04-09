var ws = new WebSocket("ws://localhost:8888/websocket");

function sendMessage(payload) {
    // Make the request to the WebSocket.
    ws.send(JSON.stringify(payload));
}

ws.onmessage = function(evt) {
    console.log(evt.data);
    $('#calendar').fullCalendar('destroy');
    initializeCalendar();
};
