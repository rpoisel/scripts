import subprocess
import os

from flask import Flask, redirect, url_for, current_app, \
        render_template, Response
from werkzeug import SharedDataMiddleware
app = Flask(__name__)

# serve static files in pic directory
app.wsgi_app = SharedDataMiddleware(app.wsgi_app,
        {'/pic': os.path.join(os.path.dirname(__file__), 'pic')})


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route("/status")
def status():
    lStatus = "not running"

    # check if process is running
    if hasattr(current_app, 'process') and \
            current_app.process != None and \
            current_app.process.poll() == None:
        lStatus = "running"

    return lStatus


@app.route("/")
def welcome():
    lStatus = None

    # check if process is running
    if hasattr(current_app, 'process') and \
            current_app.process != None and \
            current_app.process.poll() == None:
        lStatus = "Running"

    return render_template('front.html', status=lStatus)


@app.route("/play")
def play():

    # check if process can be started
    if not hasattr(current_app, 'process') or \
            current_app.process == None or \
            current_app.process.poll() != None:
        current_app.process = subprocess.Popen(
                ['dd', 'if=/dev/zero', 'of=/dev/null'])
    return redirect('/status')


@app.route("/stop")
def stop():
    # check if process is already running
    if hasattr(current_app, 'process') and \
            current_app.process != None and \
            current_app.process.poll() == None:
        current_app.process.kill()
        current_app.process = None
    return redirect('/status')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
