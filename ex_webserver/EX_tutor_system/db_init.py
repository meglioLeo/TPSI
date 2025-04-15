from app import app,db  #TODO fix impotr app
from models import Vehicle, Portal

with app.app_context():
    db.create_all()
    print("Database tables created successfully.")