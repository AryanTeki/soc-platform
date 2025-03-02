from flask import Blueprint, jsonify, request
from app.auth import auth
from app.threat_analysis import forecast_threats
from app.database import db

api = Blueprint('api', __name__)

@api.route('/threats', methods=['GET'])
def get_threats():
    threats = list(db.threats.find())
    return jsonify(threats), 200

@api.route('/forecast', methods=['POST'])
def get_forecast():
    data = request.json.get('data')  # Expecting time series data
    forecast = forecast_threats(data)
    return jsonify(forecast.tolist()), 200

@api.route('/alerts', methods=['GET'])
def get_alerts():
    alerts = list(db.alerts.find())
    return jsonify(alerts), 200

@api.route('/cases', methods=['GET'])
def get_cases():
    cases = list(db.cases.find())
    return jsonify(cases), 200

api.register_blueprint(auth) 