from pathlib import Path

from flask import Flask, render_template, send_from_directory

BASE_DIR = Path(__file__).resolve().parents[2]
APP_DIR = Path(__file__).resolve().parent

app = Flask(
    __name__,
    static_folder=str(BASE_DIR / "static"),
    static_url_path="/static",
)

@app.route('/')
def index():
    # Detta laddar filen index.html från mappen 'templates'
    return render_template('index.html')


@app.route('/src/<path:filename>')
def src_files(filename):
    return send_from_directory(APP_DIR / 'src', filename)


@app.route('/dist/<path:filename>')
def dist_files(filename):
    return send_from_directory(APP_DIR / 'dist', filename)

if __name__ == '__main__':
    app.run(debug=True)