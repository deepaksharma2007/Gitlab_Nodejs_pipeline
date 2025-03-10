from flask import Flask

import os

app = Flask(__name__)

@app.route("/")
def deep():
  return "<body  bgcolor='aqua'><h1>welcome to Deepak Sharma Server!!</h1></body>"

app.run(host='0.0.0.0' , port=8080)
