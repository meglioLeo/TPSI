from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Message(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(256), nullable=False)
    timestamp = db.Column(db.String(20), default=lambda: str(int(datetime.now().timestamp() * 1000)))

    def __repr__(self):
        return f"<Message {self.text} at {self.timestamp}>"
