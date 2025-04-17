from flask import jsonify, Flask, request
from models import db, Message
from datetime import datetime
import re
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init.app(app)

@app.route('/Messages', methods=['GET'])
def get_messages():
    message = Message.query.all()
    if not message:
        return jsonify({"error": "No message found"}), 404
    result = []
    for m in message:
        result.append({
                "text": m.text,
                "timestamp": m.timestamp
            })
    return jsonify(result), 200

@app.route('/Messages/<timestamp>', methods=['GET'])
def get_mesages_by_timestamp(timestamp):
    message = Message.query.filter_by(timestamp = timestamp).first()
    if not message:
        return jsonify({"error": "No message found"}), 404
    result = {
        "text": message.text,
        "timestamp": message.timestamp
    }
    return jsonify(result), 200

@app.route('/Message', methods=['POST'])
def register_message():
    text = request.args.get('text')
    if not text:
        return jsonify({"error": "Text is required"}), 400
    
    new_message = Message(text=text)
    db.session.add(new_message)
    db.session.commit()
    return jsonify(
       {"message": "Message registered successfully",
        "text": new_message.text,
        "timestamp": new_message.timestamp}, 201
   )
    
@app.route('/Message/<timestamp>', methods=['DELETE'])
def delete_message(timestamp):
    message = Message.query.filter_by(timestamp=timestamp).first()
    if not message:
        return jsonify({"error": "Message not found"}), 404
    
    db.session.delete(message)
    db.session.commit()
    return jsonify({"message": "Message deleted successfully"}), 200