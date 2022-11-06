from flask import Flask, jsonify

import app.compiler as compiler
import app.generator as generator

def make_app():
    app = Flask(__name__)

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    @app.route('/compute/<path:function>')
    def compute(function):

        user_function = compiler.compile_input(function)
        ulam = generator.get_spiral(user_function)

        response = jsonify(ulam)
        response.headers.add('Access-Control-Allow-Origin', '*')

        return response

    return app
