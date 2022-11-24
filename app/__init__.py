from flask import Flask
from flask_cors import CORS
from simplejson import JSONEncoder

cors = CORS()

def create_app():
    app = Flask(__name__)
    cors.init_app(app)
    app.json_encoder = JSONEncoder
    from app.main.views import main
    app.register_blueprint(main)
    
    return app