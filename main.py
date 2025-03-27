from flask import Flask
import os

from flask import send_from_directory

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Streaming de videos'


@app.route('/video/<video_name>/<file_name>')
def stream(video_name, file_name):
    video_path = os.path.join('videos', video_name)
    return send_from_directory(video_path, file_name)

@app.route('/filmes-lista')
def lista_de_filmes():
    lista = os.listdir('videos')
    return lista


if __name__ == '__main__':
    app.run()
