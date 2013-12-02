# A simple Python app

## Local development

    pip install -r requirements.txt
    python app.py

## Deploying to Stackato

    stackato push -n




#web: gunicorn --debug -b 0.0.0.0:$PORT -k flask_sockets.worker web:app

[app] 2013-11-30T13:18:10.000Z:
[app] 2013-11-30T13:18:10.000Z: 'wsgi.websocket_version': '13'} failed with AttributeError
[app] 2013-11-30T13:18:10.000Z: 'wsgi.version': (1, 0),
[app] 2013-11-30T13:18:10.000Z: AttributeError: 'WebSocket' object has no attribute 'socket'
[app] 2013-11-30T13:18:10.000Z: while ws.socket is not None:
[app] 2013-11-30T13:18:10.000Z: handler(environment)
[app] 2013-11-30T13:18:10.000Z: return self.wsgi_app(environ, start_response)
[app] 2013-11-30T13:18:10.000Z: self.application(self.environ, lambda s, h: [])
[app] 2013-11-30T13:18:10.000Z: self.run_websocket()
[app] 2013-11-30T13:18:10.000Z: self.run_application()
[app] 2013-11-30T13:18:10.000Z: Traceback (most recent call last):