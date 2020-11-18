# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 20:46:10 2020

@author: hao05
"""


# also importing the request module
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)
# home route
@app.route("/")
def home():
    return redirect(url_for("form"))

# serving form web page
@app.route("/my-form")
def form():
    return render_template('form.html')

# handling form data
@app.route('/form-handler', methods=['POST'])
def handle_data():
    print(""*20)
    print(request.form)
    print(""*20)
    print(request.method)
    
    name = request.form['name']
    gender = request.form['gender']
    station = request.form['Station']

    return render_template(station+'.html')

if __name__ == "__main__":
    app.run(debug = True) 
