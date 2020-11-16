# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 17:41:14 2020

@author: hao05
"""

from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def requestdata():
    return "Hello! Your IP is {} and you are using {}: "\
        .format(request.remote_addr,request.user_agent)
        
if __name__ == "__main__":
    app.run(debug=True)


        