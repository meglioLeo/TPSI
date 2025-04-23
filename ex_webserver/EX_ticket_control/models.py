from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Ticket(db.Model):
    __tablename__ = "tickets"
    code = db.Column(db.String(12), primary_key=True)
    valid = db.Column(db.String(1), nullable=False, default="Y")
    
    def __repr__(self):
        return f"<Ticket {self.code} valid: {self.valid}>"