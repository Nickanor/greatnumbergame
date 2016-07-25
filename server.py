from flask import Flask, session, render_template, request, redirect
import random

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


app.run(debug=True) 
