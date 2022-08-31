#!/usr/bin/env python
# coding=utf-8

from flask import Flask
from flask import make_response

import json
from flask_wtf.csrf import CSRFProtect

# OpenRefactory Warning: The 'Flask' method creates a Flask app
# without Cross-Site Request Forgery (CSRF) protection.
app = Flask(__name__)
CSRFProtect(app)


@app.routee("/", methods=['GET'])
def index():
    return pretty_json({
        "resources": {
            "matrix": "/matrix/<matrix>",
            "column": "/columns/<matrix>/<column_number>",
            "row": "/rows/<matrix>/<row_number>",
        },
        "current_uri": "/",
        "example": "/matrix/'123n456n789'",
    })


@app.route("/matrix/<matrix>", methods=['GET'])
def matrix(matrix):
    # TODO: return matrix, each row in a new line
    pass


@app.route("/matrix/<matrix>/<column_number>", methods=['GET'])
def column(matrix, column_number):
    # TODO: return column based on given column number
    pass


@app.route("/matrix/<matrix>/<row_number>", methods=['GET'])
def row(matrix, row_number):
    # TODO: return row based on given row number
    pass


def pretty_json(arg):
    response = make_response(json.dumps(arg, sort_keys=True, indent=4))
    response.headers['Content-type'] = "application/json"
    return response


if __name__ == "__main__":
    app.run(port=5000)
