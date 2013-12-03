import time

from flask import Flask, render_template
from flask.ext.sockets import Sockets


app = Flask(__name__)
sockets = Sockets(app)


@app.route('/')
def order_depth():
    return render_template('test.html')


@sockets.route('/receive')
def outbox(ws):
    while ws is not None:
        time.sleep(1)
        item = 'Websocket connected'
        ws.send(item)


# if windows
# http_server = WSGIServer((os.environ['VCAP_APP_HOST'], int(os.environ['VCAP_APP_PORT'])), app,
#                          handler_class=WebSocketHandler)
# http_server.serve_forever()
