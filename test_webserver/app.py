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
            "id": city.id,
            "name": city.name,
            "country": city.country,
            "area": city.area,
            "last_detection": city.last_detection
        })

    return jsonify(result), 200

# Get specific city by id
@app.route('/city', methods=['GET'])
def get_city_by_id(id):
    city = City.query.filter_by(id=id).first()

    if not city:
        return jsonify({"error": "City not found"}), 404
    
    result = {
        "id": city.id,
        "name": city.name,
        "country": city.country,
        "area": city.area,
        "last_detection": city.last_detection
    }

    return jsonify(result), 200

# Register new city
@app.route('/city', methods=['POST'])
def register_city():
    data = request.get_json()
    if  not data or "name" not in data or "country" not in data or "area" not in data or "last_detection" not in data:
        return jsonify({{"error": "Name, country, area and last detection are required"}}), 400
    
    new_city = City(
        name = data['name'],
        country = data['country'],
        area = data['area'],
        last_detection = data['last_detection']
    )

    db.session.add(new_city)
    db.session.commit()

    return jsonify({"message": "City registered successfully"}), 201

# Update city
@app.route('/city', methods=['PUT'])
def update_city(id):
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    city = City.query.filter_by(id=id).first()
    if not city:
        return jsonify({"error": "City not found"}), 404

    if 'name' in data:
        city.name = data['name']
    if 'country' in data:
        city.country = data['country']
    if 'area' in data:
        city.area = data['area']
    if 'last_detection' in data:
        city.last_detection = data['last_detection']

    db.session.commit()

    return jsonify({"message": "City updated successfully"}), 200

# Delete city
@app.route('/city', methods=['DELETE'])
def delete_city(id):
    city = City.query.filter_by(id=id).first()

    if not city:
        return jsonify({"error": "City not found"}), 404
    
    db.session.delete(city)
    db.session.commit()

    return jsonify({"message": "City deleted successfully"}), 200