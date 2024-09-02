from flask import Flask, request, render_template
import gunicorn
import platform
import subprocess

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!\n" + "Python version: " + platform.python_version() + "\n"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080
