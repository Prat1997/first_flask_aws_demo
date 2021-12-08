from flask import Flask
import flask
application=Flask(__name__)

@application.route('/')
def hello_world():
    return "Hello , This is prateek's first elastic bean stalk project but Third commit"
