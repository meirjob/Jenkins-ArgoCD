from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Two things define you: your patience when you have nothing and your attitude when you have everything.'
