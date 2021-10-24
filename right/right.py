import turtle
import requests
from flask import Flask

app = Flask(__name__)

host_port = 7000
dest_port = 6000


@app.route('/ping')
def do_pong():
    res = ''
    try:
        res = requests.get(f'ping_container:{dest_port}/pong')
    except requests.exceptions.RequestException as e:
        print('error')
        return 'pong fail\n'

    return 'pong' + str(res) + '\n'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=host_port)
