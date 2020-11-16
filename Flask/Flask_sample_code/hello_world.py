# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 15:05:25 2020

@author: hao05
"""

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'


@app.route('/career/')
def career():
    return 'Career Page'


@app.route('/contact/')
@app.route('/feedback/')
def feedback():
    return 'Feedback Page'


@app.route('/user/<id>/')
def user_profile(id):
    return "Profile page of user #{}".format(id)


if __name__ == "__main__":
    app.run()
    
    
