from flask import Flask, request, jsonify
from models import db, Vehicle, Portal
from datetime import datetime
import re
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

# Helper function to check if a vehicle is from emergency or law enforcement
def is_emergency_or_law_enforcement(license_plate):
    """Checks if the license plate belongs to an emergency or law enforcement vehicle"""
    return re.match(r"^(CC|EI)\s[a-zA-Z]{3}\s\d{2}$", license_plate) is not None

# Route for registering vehicle entry into the monitored area
@app.route('/register_entry', methods=['POST'])
def register_entry():
    """Registers a vehicle when it enters the monitored area"""
    data = request.json
    license_plate = data.get('license_plate')
    portal_id = data.get('portal_id')
    # Validate input
    if not license_plate or not portal_id:
        return jsonify({"error": "License plate and portal ID are required"}), 400
    if is_emergency_or_law_enforcement(license_plate):
        return jsonify({"error": "Cannot register emergency or law enforcement vehicles"}), 403
    
    # Check if the portal exists
    portal = Portal.query.filter_by(portal_id=portal_id).first()
    if not portal:
        return jsonify({"error": "Portal not found"}), 404
    
    # Register vehicle entry
    timestamp = datetime.now()
    new_vehicle = Vehicle(
    license_plate=license_plate,

    portal_id=portal.id,
    timestamp_in=timestamp
    )
    
    db.session.add(new_vehicle)
    db.session.commit()
    return jsonify({"message": "Vehicle registered successfully", "timestamp": timestamp.isoformat()}), 200

# Route for updating vehicle exit from the monitored area
@app.route('/register_exit', methods=['POST'])
def register_exit():
    """Updates a vehicle record when it exits the monitored area"""
    data = request.json
    license_plate = data.get('license_plate')
    portal_id = data.get('portal_id')
    # Validate input
    if not license_plate or not portal_id:
        return jsonify({"error": "License plate and portal ID are required"}), 400
    if is_emergency_or_law_enforcement(license_plate):
        return jsonify({"error": "Cannot register emergency or law enforcement vehicles"}), 403
    vehicle = Vehicle.query.filter_by(license_plate=license_plate, portal_id=portal_id).first()
    if not vehicle:
        return jsonify({"error": "Vehicle entry not found"}), 404
    # Update exit timestamp
    vehicle.timestamp_out = datetime.now()
    db.session.commit()
    return jsonify({"message": "Vehicle exit updated successfully", "timestamp_out":
    vehicle.timestamp_out.isoformat()}), 200
    
# Route for getting all portal data for a specific vehicle
@app.route('/get_portals/<license_plate>', methods=['GET'])
def get_portals(license_plate):
    """Returns all portals where a vehicle has been detected"""
    vehicle = Vehicle.query.filter_by(license_plate=license_plate).all()
    if not vehicle:
        return jsonify({"error": "Vehicle not found"}), 404
    result = []
    for v in vehicle:
        result.append({
    "portal_id": v.portal.portal_id,
    "timestamp_in": v.timestamp_in.isoformat(),
    "timestamp_out": v.timestamp_out.isoformat() if v.timestamp_out else None
    })
    return jsonify(result), 200

# Route for deleting records of emergency/law enforcement vehicles
@app.route('/delete_record/<license_plate>', methods=['DELETE'])
def delete_record(license_plate):
    """Deletes the record for emergency or law enforcement vehicles"""
    if not is_emergency_or_law_enforcement(license_plate):
        return jsonify({"error": "Vehicle is not emergency or law enforcement"}), 403
    vehicle = Vehicle.query.filter_by(license_plate=license_plate).first()
    if not vehicle:
        return jsonify({"error": "Vehicle record not found"}), 404
    db.session.delete(vehicle)
    db.session.commit()
    return jsonify({"message": "Vehicle record deleted successfully"}), 200

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)