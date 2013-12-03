var inbox = new ReconnectingWebSocket("ws://localhost:8000/receive");

inbox.onmessage = function (message) {
    $(".connected-text").append('<p>' + message.data + '</p>');
    console.log(message.data)
};

