from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'index'

if __name__ == '__main__':
    app.run("127.0.0.1", port=5000, debug=True)
