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