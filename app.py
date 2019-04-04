# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 10:46:02 2019

@author: Jessie
"""

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
