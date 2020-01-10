from bottle import Bottle, request, response, abort, JSONPlugin
from geventwebsocket import WebSocketError
import os, json
from time import sleep
from bson import json_util
from db import DB
import datetime
from random import seed, randint
import slack

app = Bottle()
app.install(JSONPlugin(json_dumps=lambda body: json.dumps(body, default=json_util.default)))
db = DB()
#client = slack.WebClient(token=os.getenv(<SLACK_API_TOKEN>))

seed(1)

@app.hook('after_request')
def enable_cors():
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Authorization, Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token, Accept-Encoding, Content-Disposition, Content-Length, Accept-Ranges, Content-Range'


@app.route('/', method='OPTIONS')
@app.route('/<path:path>', method='OPTIONS')
def options_handler(path=None):
    return

def _update_rota_if_needed(rota):
    day_no = randint(0,10)
    print(day_no)
    #day_no = datetime.datetime.today().weekday()
    if day_no > 4:
        db.update(rota['next']['team'], {'is_on_call': 1})
        db.update(rota['current']['team'], {'is_on_call': 0})
        rota = db.fetch_on_call_rota()
        #client.chat_postMessage(channel=rota['current']['channel'], text="{} is on-call this week!".format(rota['current']['team']))
    return rota

@app.route('/', method='GET')
def get():
    rota = db.fetch_on_call_rota()
    # rota = _update_rota_if_needed(rota)
    return rota


@app.route('/websocket')
def handle_websocket():
    wsock = request.environ.get('wsgi.websocket')
    if not wsock:
        abort(400, 'Expected WebSocket request.')
    rota = db.fetch_on_call_rota()

    while True:
        try:
            rota = _update_rota_if_needed(rota)
            wsock.send(json.dumps(rota))
            sleep(30)
        except WebSocketError:
            break