from flask import Flask, jsonify, request
from models import db, Museum
from config import Config
from datetime import datetime

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

# Register a new museum
@app.route('/museums', methods=['POST'])
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