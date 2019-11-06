import logging
import subprocess

from flask import Flask
from flask_restful import Resource, Api, reqparse

logger = logging.getLogger("")  # todo : logger 기능 추가

app = Flask(__name__)
api = Api(app)
proc = None

# parser = reqparse.RequestParser()
# parser.add_argument('--host', type=str, default="cw.cloa.io",
#                         help='type host')
# parser.add_argument('--port', type=int, default=4242,
#                         help='type port')
# parser.add_argument('--query_time', type=int, default=1,
#                         help='type query time')
# parser.add_argument('--db', type=str, default="maria",
#                         help='type query time')
# args = parser.parse_args()

# 1. run
class start_worker(Resource):
    def post(self):
        global proc
        proc = subprocess.Popen(['python worker.py'], shell=True)
        return {'result': 'worker started'}


# 2. stop
class stop_worker(Resource):
    def post(self):
        global proc
        proc.terminate()
        proc = None
        return {'result': 'worker stopped'}


# 3. modify arguments
# stop and rerun
class modify_worker(Resource):
    def post(self, query_time):
        global proc
        if proc:
            proc.terminate()
        proc = subprocess.Popen([f'python worker.py --query_time={query_time}'], shell=True)
        return {'result': 'worker restarted'}


api.add_resource(start_worker, '/start')
api.add_resource(stop_worker, '/stop')
api.add_resource(modify_worker, '/modify/<int:query_time>')


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
