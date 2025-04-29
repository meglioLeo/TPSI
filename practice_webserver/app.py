from flask import Flask, jsonify, request
from models import db, Museum
from config import Config
from datetime import datetime

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

# Register a new museum
@app.route('/register_museum', methods=['POST'])
def register_museum():
    data = request.get_json()
    if not data or 'name' not in data or 'city' not in data or 'country' not in data:
        return jsonify({"error": "Name, city, and country are required"}), 400

    name = data['name']
    city = data['city']
    country = data['country']
    annual_visitors = data.get('annual_visitors')
    foundation_date = data.get('foundation_date')
    exhibition_area = data.get('exhibition_area')

    new_museum = Museum(
        name=name,
        city=city,
        country=country,
        annual_visitors=annual_visitors,
        foundation_date=foundation_date,
        exhibition_area=exhibition_area
    )
    
    db.session.add(new_museum)
    db.session.commit()
    
    return jsonify({"message": "Museum registered successfully"}), 201

# Get all museums
@app.route('/get_museums', methods=['GET'])
def get_museums():
    museums = Museum.query.all()
    
    if not museums:
        return [], 200
    
    result = []
    for museum in museums:
        result.append({
            "id": museum.id,
            "name": museum.name,
            "city": museum.city,
            "country": museum.country,
            "annual_visitors": museum.annual_visitors,
            "foundation_date": museum.foundation_date,
            "exhibition_area": museum.exhibition_area
        })
        
    return jsonify(result), 200

# Get a specific museum by ID
@app.route('/get_museum/<id>', methodS=['GET'])
def get_museum(id):
    museum = Museum.query.filter_by(id=id).first()
    if not museum:
        return jsonify({"error": "Museum not found"}), 404
    result = {
        "id": museum.id,
        "name": museum.name,
        "city": museum.city,
        "country": museum.country,
        "annual_visitors": museum.annual_visitors,
        "foundation_date": museum.foundation_date,
        "exhibition_area": museum.exhibition_area
    }
    
    return jsonify(result), 200

# Update a museum's information
@app.route('/update_museum/<id>', methods=['PUT'])
def update_museum(id):
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    museum = Museum.query.filter_by(id=id).first()
    if not museum:
        return jsonify({"error": "Museum not found"}), 404

    if 'name' in data:
        museum.name = data['name']
    if 'city' in data:
        museum.city = data['city']
    if 'country' in data:
        museum.country = data['country']
    if 'annual_visitors' in data:
        museum.annual_visitors = data['annual_visitors']
    if 'foundation_date' in data:
        museum.foundation_date = data['foundation_date']
    if 'exhibition_area' in data:
        museum.exhibition_area = data['exhibition_area']

    db.session.commit()
    
    return jsonify({"message": "Museum updated successfully"}), 200