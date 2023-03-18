from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World, welcome!! Project by Obinna Aliogor, IT is the Future, TY!!!'
