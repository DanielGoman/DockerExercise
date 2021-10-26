import requests
from flask import Flask
import time

app = Flask(__name__)

host_port = 6000
dest_port = 7000


@app.route('/pong')
def do_ping():
    res = ''
    time.sleep(1)
    try:
        print('sent ping')
        res = requests.get(f'http://localhost:{dest_port}/ping')
        print('-> answered ping')
    except requests.exceptions.RequestException as e:
        print('rip')
        return 'ping fail'

    return 'ping ' + str(res) + '\n'


if __name__ == "__main__":
    app.run(host='localhost', port=host_port)
