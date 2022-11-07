from flask import Flask
from config import config
from flask_cors import CORS
from dotenv import load_dotenv

# Routes
from routes import Publication, auth

app = Flask(__name__)
CORS(app, resources={"*":{"origins":"http://localhost:3000"}}) #para react, 9300 para webpack

def page_not_found(error):
    return '<h1>Page Not Found</h1>', 404

if __name__ == '__main__':
    load_dotenv()
    app.config.from_object(config['development'])

    # Blueprints
    app.register_blueprint(auth.routes_auth, url_prefix = '/api')
    app.register_blueprint(Publication.main, url_prefix = '/api/publication')

    # error handlers
    app.register_error_handler(404, page_not_found)
    app.run()
