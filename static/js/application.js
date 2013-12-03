var inbox = new ReconnectingWebSocket("ws://stackato-sockets.192.168.0.120.xip.io/receive");

inbox.onmessage = function (message) {
    $(".connected-text").append('<p>' + message.data + '</p>');
    console.log(message.data)
};

