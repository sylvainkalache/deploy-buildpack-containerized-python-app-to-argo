from flask import Flask, request, render_template
import gunicorn
import platform
import subprocess

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World using pack build!\n Pushing a new feature \n" + "Python version: " + platform.python_version() + "\n"
