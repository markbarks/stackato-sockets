import time

from flask import Flask, render_template
from flask.ext.sockets import Sockets


app = Flask(__name__)
sockets = Sockets(app)


@app.route('/')
def order_depth():
    return render_template('order_depth.html')


@sockets.route('/receive')
def outbox(ws):
    print ws
    while ws.socket is not None:
        time.sleep(1)
        item = 'Websocket connected'
        ws.send(item)


# if windows
# os.environ['VCAP_APP_HOST'] = '0.0.0.0'
# os.environ['VCAP_APP_PORT'] = '8000'
# http_server = WSGIServer((os.environ['VCAP_APP_HOST'], int(os.environ['VCAP_APP_PORT'])), app,
#                          handler_class=WebSocketHandler)
# http_server.serve_forever()
