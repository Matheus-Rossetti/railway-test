from flask import Flask, jsonify
import os

from supabase import create_client, Client


url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")


supabase: Client = create_client(url, key)

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Streaming de videos'


@app.route('/video/<video_name>/<file_name>')
def stream(video_name, file_name):

    return

@app.route('/filmes-lista')
def lista_de_filmes():
    response = supabase.storage.list_buckets()
    return jsonify(response)


def supa():
    response = supabase.storage.list_buckets()

    print(response)


if __name__ == '__main__':
    app.run()

