from bottle import Bottle, request, response, abort, JSONPlugin
from geventwebsocket import WebSocketError
import os, json
from time import sleep
from bson import json_util

app = Bottle()
app.install(JSONPlugin(json_dumps=lambda body: json.dumps(body, default=json_util.default)))

@app.hook('after_request')
def enable_cors():
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Authorization, Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token, Accept-Encoding, Content-Disposition, Content-Length, Accept-Ranges, Content-Range'


@app.route('/', method='OPTIONS')
@app.route('/<path:path>', method='OPTIONS')
def options_handler(path=None):
    return


@app.route('/', method='GET')
def get():
    return { "data": [ {"title": "I\'m Batman", "start": "2019-12-02", "end": "2019-12-05", "info": {"who": "Batman"} } ] }


# @app.route('/websocket')
# def handle_websocket():
#     wsock = request.environ.get('wsgi.websocket')
#     if not wsock:
#         abort(400, 'Expected WebSocket request.')

#     while True:
#         try:
#             num = db_mgr.get_num_of_due_machines()
#             wsock.send(json.dumps(num))
#             sleep(60)
#         except WebSocketError:
#             break