from gevent import monkey
monkey.patch_all()
import bottle, os
from bottle import run
from gevent.pywsgi import WSGIServer
from geventwebsocket import WebSocketError
from geventwebsocket.handler import WebSocketHandler
from modules import event

route_prefix = '/alfred-api'

app = bottle.app()
app.mount(route_prefix + '/event', event.app)
if os.environ.get('APP_LOCATION') == 'heroku':
    run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), server='gevent', handler_class=WebSocketHandler)
else:
    run(host='localhost', port=8080, debug=True, server='gevent', handler_class=WebSocketHandler)
