import requests
from flask import Flask
import time

app = Flask(__name__)

host_port = 7000
dest_port = 6000


@app.route('/ping')
def do_ping():
    res = ''
    time.sleep(1)
    try:
        print('sent pong')
        res = requests.get(f'http://localhost:{dest_port}/pong')
        print('-> answered pong')
    except requests.exceptions.RequestException as e:
        print(e)
        return 'pong fail'

    print('ponggggg')
    return 'pong ' + str(res) + '\n'


if __name__ == "__main__":
    app.run('localhost', port=host_port)