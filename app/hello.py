# -*- coding:utf-8 -*-

import platform
import subprocess
import time
from webbot import Browser
from flask import Flask, Response, request
app = Flask(__name__)

@app.route("/")
def headers():
    return '<br/>'.join(['%s => %s' % (key, value) for (key, value) in request.headers.items()])

@app.route("/favicon.ico")
def favicon():
    resp = Response(status=200, mimetype='image/png')
    return resp

@app.route("/pyver")
def pyver():
    return platform.python_version()

@app.route("/app")
def app1():
  time.sleep(1)
  print("Installation complete!")
  print("Please wait...")
  time.sleep(3)
  print("Starting...")
  Chromium = Browser()
  print("Finished!")
print("Chromium is now ready to use!")

if __name__ == "__main__":
    app.run()

