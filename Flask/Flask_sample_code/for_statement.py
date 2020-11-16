# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 23:25:28 2020

@author: hao05
"""

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def stat_for():
    return render_template('for statement.html', num_list=[1,4,7,8,5,2])

if __name__ == "__main__":
    app.run(debug=True)