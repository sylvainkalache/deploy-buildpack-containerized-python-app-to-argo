from flask import Flask, request, render_template
import gunicorn
import platform
import subprocess

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World using pack build!\n Argo is working? \n" + "Python version: " + platform.python_version() + "\n"
