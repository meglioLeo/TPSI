from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Museum(db.Model):
    __tablename__ = 'museums'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    annual_visitors = db.Column(db.Integer)
    foundation_date = db.Column(db.Date)  
    exhibition_area = db.Column(db.Float)

    def __repr__(self):
        return f"<Museum {self.name} in {self.city}, {self.country}>"