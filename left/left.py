import turtle
import requests
from flask import Flask

app = Flask(__name__)

host_port = 6000
dest_port = 7000


@app.route('/pong')
def do_ping():
    res = ''
    try:
        res = requests.get(f'pong_container:{dest_port}/ping')
    except requests.exceptions.RequestException as e:
        print('error')
        return 'ping fail\n'

    return 'ping' + str(res) + '\n'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=host_port)
