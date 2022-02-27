#!/usr/bin/env python
import flask
import time
import re
import os

app = flask.Flask(__name__)

@app.route('/welcome', methods=['GET'])
def welcome():
    return "you have reached Baqar heroku server :)",200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=18000, use_reloader=False)

