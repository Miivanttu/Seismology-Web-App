from datetime import datetime
from . import db

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    kuupaev = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)  # Date field
    vertikaalne = db.Column(db.Float, nullable=False)  # Vertical field (can be float)
    horisontaalne = db.Column(db.Float, nullable=False)  # Horizontal field (can be float)
    piki = db.Column(db.Float, nullable=False)  # Longitudinal field (can be float)
    risti = db.Column(db.Float, nullable=False)  # Transverse field (can be float)
    vektor_summa = db.Column(db.Float, nullable=False)  # Vector sum field (can be float)

    def __repr__(self):
        return f"Data('{self.kuupaev}', '{self.vertikaalne}', '{self.horisontaalne}', '{self.piki}', '{self.risti}', '{self.vektor_summa}')"