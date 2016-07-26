from flask import Flask, session, render_template, request, redirect
import random

app=Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def index():
    try:
        session['random']
    except:
        session['random'] = random.randrange(1,101)
    print session['random']
    return render_template('index.html')

@app.route('/check', methods=['POST'])


app.run(debug=True)
