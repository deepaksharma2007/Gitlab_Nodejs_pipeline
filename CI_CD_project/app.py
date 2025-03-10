from flask import Flask

import os

app = Flask(_name_)

@app.route("/")
def deep():
   return "welcome to Deepak Sharma Server! !"

app.run(host='0.0.0.0' , port=8080)
