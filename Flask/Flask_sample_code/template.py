# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 23:19:39 2020

@author: hao05
"""

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def template():
    return render_template('template.html', name='Song Song Hao')

if __name__ == "__main__":
    app.run(debug=True)
    
    
