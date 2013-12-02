# import os
import logging
from flask import Flask, render_template
from flask.ext.sockets import Sockets
import time

# from gevent.pywsgi import WSGIServer
# from geventwebsocket import WebSocketHandler
# from flask_sockets import Sockets


app = Flask(__name__)
sockets = Sockets(app)


@app.route('/')
def order_depth():
    logging.info('Returning order depth template')
    return render_template('order_depth.html')

#
# q = Queue()


@sockets.route('/receive')
def outbox(ws):
    print ws
    while ws.socket is not None:
        # item = q.get(block=True)
        # ob = convert_ob(item)
        time.sleep(1)
        item = 'Websocket connected'
        ws.send(item)


# def receive_command():
#     connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
#     channel = connection.channel()
#     channel.queue_declare(queue='mli')
#
#     def callback_rabbit(ch, method, properties, body):
#         q.put(body)
#
#     channel.basic_consume(callback_rabbit, queue='mli', no_ack=True)
#     channel.start_consuming()
#
#
# def start_consumer():
#     t = threading.Thread(target=receive_command)
#     t.setDaemon(True)
#     t.start()
#
#
# consumer_thread = start_consumer()

# if windows
# os.environ['VCAP_APP_HOST'] = '0.0.0.0'
# os.environ['VCAP_APP_PORT'] = '8000'
# http_server = WSGIServer((os.environ['VCAP_APP_HOST'], int(os.environ['VCAP_APP_PORT'])), app,
#                          handler_class=WebSocketHandler)
# http_server.serve_forever()
