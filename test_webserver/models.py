from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class City(db.Model):
    __tablename__ = "cities"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    country = db.Column(db.String(100), nullable = False)
    area = db.Column(db.Float, nullable = False)
    last_detection = db.Column(db.String, nullable = False)   # YYYY-MM-DD format

    def __repr__(self):
        return f"<City: {self.name} in {self.country}>"