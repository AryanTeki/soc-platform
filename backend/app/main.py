from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from app.routes import api
from app.database import init_db

app = Flask(__name__)
CORS(app)

# Load configuration
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'
jwt = JWTManager(app)

# Initialize database
init_db()

# Register API routes
app.register_blueprint(api)

if __name__ == '__main__':
    app.run(debug=True) 