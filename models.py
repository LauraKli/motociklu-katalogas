from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Kategorija(db.Model):
    __tablename__ = 'kategorija'

    id = db.Column(db.Integer, primary_key=True)

    pavadinimas = db.Column(db.String(50), nullable=False)
    motociklai = db.relationship('Motociklas', backref='kategorija', lazy=True)

class Motociklas(db.Model):
    __tablename__ = 'motociklas'

    id = db.Column(db.Integer, primary_key=True)
    modelis = db.Column(db.String(100), nullable=False)
    kaina = db.Column(db.Float, nullable=False)
    pagaminimo_metai = db.Column(db.Integer, nullable=False)
    gamintojas = db.Column(db.String(100), nullable=False)
    galia_kw = db.Column(db.Float, nullable=False)
    aprasymas = db.Column(db.Text, nullable=True)
    nuotrauka_url = db.Column(db.String(200), nullable=True)
    kategorija_id = db.Column(db.Integer, db.ForeignKey('kategorija.id'), nullable=False)
