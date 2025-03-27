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
    with open(f"./{video_name}/{file_name}", "wb+") as f:
        response = (
            supabase.storage
            .from_("videos")
            .download(f"{video_name}/{file_name}")
        )
        f.write(response)
    return jsonify(f)

@app.route('/lista-de-videos')
def arquivos_do_balde():
    response = (
        supabase.storage
        .from_("videos")
        .list(
            "folder",
            {
                "limit": 100,
                "offset": 0,
                "sortBy": {"column": "name", "order": "desc"},
            }
        )
    )
    return jsonify(response)




if __name__ == '__main__':
    app.run()

