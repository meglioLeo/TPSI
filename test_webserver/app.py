from flask import Flask, jsonify, request
from models import db, City
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

# Get all cities endpoint
@app.route('/cities', methods=['GET'])
def get_cities():
    cities = City.query.all()

    if not cities:
        return [], 200   #no city registered, no need to return a 404
    
    result = []

    for city in cities:
        result.append({
            "ID": city.ID,
            "name": city.name,
            "country": city.country,
            "area": city.area,
            "last_detection": city.last_detection
        })

    return jsonify(result), 200