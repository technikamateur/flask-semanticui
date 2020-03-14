from flask import Flask
from flask_semanticui import SemanticUI


def create_app():
    app = Flask(__name__)
    SemanticUI(app)

    @app.route('/')
    def hello():
        return 'Hello, World!'
    
    return app