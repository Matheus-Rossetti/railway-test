from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Streaming de videos'


@app.route('/video/<video_name>/<file_name>')
def stream(video_name, file_name):

    return jsonify(f'Seu video deveria estar baixando: {video_name} | {file_name}')

@app.route('/lista-de-videos')
def arquivos_do_balde():



    return



if __name__ == '__main__':
    app.run()

