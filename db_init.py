from flask import Flask
from models import db, Kategorija, Motociklas
import os
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/Vartotojas/Desktop/motociklu katalogas/katalogas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    if os.path.exists('C:/Users/Vartotojas/Desktop/motociklu katalogas/katalogas.db'):
        os.remove('C:/Users/Vartotojas/Desktop/motociklu katalogas/katalogas.db')
    db.create_all()
    print("📦 Duomenų bazės lentelės sukurtos")

    kategorijos = [
        Kategorija(pavadinimas='Street'),
        Kategorija(pavadinimas='Cruiser'),
        Kategorija(pavadinimas='Sport'),
        Kategorija(pavadinimas='Touring'),
        Kategorija(pavadinimas='Adventure'),
        Kategorija(pavadinimas='Electric')
    ]

    db.session.add_all(kategorijos)
    db.session.commit()
    motociklai = [
        Motociklas(
            modelis='Yamaha MT-07',
            kaina=7500,
            pagaminimo_metai=2022,
            gamintojas='Yamaha',
            galia_kw=55.0,
            aprasymas='Lengvas ir galingas motociklas miesto kelionėms.',
            nuotrauka_url='static/images/yamaha_mt07.jpg',
            kategorija_id=1
        ),
        Motociklas(
            modelis='Honda Rebel 500',
            kaina=6800,
            pagaminimo_metai=2021,
            gamintojas='Honda',
            galia_kw=34.0,
            aprasymas='Stilingas motociklas, puikiai tinkantis pradedantiesiems.',
            nuotrauka_url='static/images/honda_rebel_500.jpg',
            kategorija_id=2
        )
    ]

    db.session.add_all(motociklai)
    db.session.commit()

    print("✅ Duomenų bazė sukurta ir užpildyta!")