from flask import Flask, jsonify, request
from models import db, City
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

