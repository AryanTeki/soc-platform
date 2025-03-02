from flask import Flask
from flask_cors import CORS
from app.auth import auth
from app.routes import api

app = Flask(__name__)
CORS(app)

app.register_blueprint(auth)
app.register_blueprint(api)

if __name__ == '__main__':
    app.run(debug=True)
