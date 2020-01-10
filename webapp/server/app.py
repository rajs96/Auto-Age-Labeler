# script that creates the app
from flask import Flask
import os

def create_app():
    app = Flask(__name__)

    from routes.files import file_api as file_blueprint

    app.register_blueprint(file_blueprint, url_prefix='/api')

    return app
if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0',port=5000,threaded=False)
