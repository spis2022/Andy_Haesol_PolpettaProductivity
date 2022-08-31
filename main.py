from flask import Flask
from flask import render_template
from flask import request
import random
app = Flask(__name__)


@app.route('/')

def render_home():

    return render_template('home.html')

@app.route('/timer')

def render_timer():

    return render_template('timer.html')

@app.route('/cool')
def render_cool():

    return render_template('cool.html')
if __name__ == "__main__":

   app.run(host='0.0.0.0')
    
    