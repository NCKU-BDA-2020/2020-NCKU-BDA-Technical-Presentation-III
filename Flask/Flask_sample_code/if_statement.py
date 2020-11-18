# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 23:25:22 2020

@author: hao05
"""

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def stat_if():
    return render_template('if statement.html', name='Song Song Hao', gender='Male')

if __name__ == "__main__":
    app.run(debug=True)