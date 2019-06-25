import sys
import signal
from flask import Flask


def sigterm_handler(*args):
    [print(a) for a in args]
    sys.exit()


signal.signal(signal.SIGTERM, sigterm_handler)

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"
