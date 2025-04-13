from models import db, Motociklas, Kategorija
from app import app

motociklai = [
    # 🟦 STREET
    ("Yamaha MT-07", "Yamaha", 7500, 2022, 55.0, "Lengvas, manevringas motociklas su galingu dviejų cilindrų varikliu.", "static/images/yamaha_mt07.jpg", "Street"),
    ("KTM Duke 390", "KTM", 5700, 2022, 32.0, "Agresyvus, bet kompaktiškas miesto motociklas.", "static/images/ktm_duke_390.jpg", "Street"),
    ("Suzuki SV650", "Suzuki", 7200, 2021, 56.0, "Legendinis V-Twin motociklas viskam.", "static/images/suzuki_sv650.jpg", "Street"),
    ("Benelli TNT 300", "Benelli", 4500, 2020, 28.0, "Itališkas dizainas ir prieinama kaina.", "static/images/benelli_tnt_300.jpg", "Street"),

    # 🟥 CRUISER
    ("Honda Rebel 500", "Honda", 6800, 2021, 34.0, "Stilingas cruiser tipo motociklas, puikiai tinkantis pradedantiesiems.", "static/images/honda_rebel_500.jpg", "Cruiser"),
    ("Harley-Davidson Iron 883", "Harley-Davidson", 9700, 2020, 37.0, "Klasikinis Harley dizainas ir garsas su galingu V-Twin varikliu.", "static/images/harley_iron_883.jpg", "Cruiser"),
    ("Yamaha Bolt", "Yamaha", 8800, 2022, 40.0, "Mažas, bet tvirtas cruiser'is.", "static/images/yamaha_bolt.jpg", "Cruiser"),
    ("Indian Scout Bobber", "Indian", 11200, 2023, 70.0, "Amerikietiškas stilius ir jėga.", "static/images/indian_scout_bobber.jpg", "Cruiser"),

    # 🟩 SPORT
    ("Kawasaki Ninja 650", "Kawasaki", 8300, 2023, 50.2, "Sportinis motociklas su agresyviu dizainu ir puikiu valdymu.", "static/images/kawasaki_ninja_650.jpg", "Sport"),
    ("Yamaha R3", "Yamaha", 6700, 2022, 31.0, "Lengvas, greitas, pradedantiesiems.", "static/images/yamaha_r3.jpg", "Sport"),
    ("KTM RC 390", "KTM", 6900, 2022, 32.0, "Sportiškas dizainas ir valdymas.", "static/images/ktm_rc_390.jpg", "Sport"),
    ("Aprilia RS 660", "Aprilia", 12200, 2023, 74.0, "Modernus, dinamiškas ir stilingas.", "static/images/aprilia_rs660.jpg", "Sport"),

    # 🟨 TOURING
    ("BMW R1250RT", "BMW", 18000, 2022, 100.0, "Aukščiausios klasės touring motociklas ilgiems maršrutams.", "static/images/bmw_r1250rt.jpg", "Touring"),
    ("Honda Gold Wing", "Honda", 23000, 2022, 93.0, "Kelionės limuzinas su komfortu.", "static/images/honda_gold_wing.jpg", "Touring"),
    ("Yamaha FJR1300", "Yamaha", 14900, 2021, 107.0, "Greitas ir patogus ilgam nuvažiavimui.", "static/images/yamaha_fjr1300.jpg", "Touring"),
    ("BMW K1600 GT", "BMW", 24500, 2023, 118.0, "Galingas šešių cilindrų keliautojas.", "static/images/bmw_k1600gt.jpg", "Touring"),

    # 🟧 ADVENTURE
    ("Suzuki V-Strom 650", "Suzuki", 8600, 2021, 52.0, "Universalus adventure tipo motociklas su patogiu važiuoklės aukščiu.", "static/images/suzuki_vstrom_650.jpg", "Adventure"),
    ("Yamaha Tenere 700", "Yamaha", 9900, 2022, 54.0, "Idealiai pritaikytas bekelėms ir ilgoms kelionėms.", "static/images/yamaha_tenere_700.jpg", "Adventure"),
    ("Honda Africa Twin", "Honda", 13300, 2023, 75.0, "Legendinis bekelės nuotykių motociklas.", "static/images/honda_africa_twin.jpg", "Adventure"),
    ("KTM 890 Adventure", "KTM", 14200, 2023, 78.0, "Modernus ir galingas nuotykių motociklas.", "static/images/ktm_890_adventure.jpg", "Adventure"),

    # 🟪 ELECTRIC
    ("Zero SR/F", "Zero Motorcycles", 19000, 2022, 82.0, "Galingas elektrinis motociklas su moderniu dizainu ir momentiniu sukimo momentu.", "static/images/zero_srf.jpg", "Electric"),
    ("Energica Eva Ribelle", "Energica", 26500, 2023, 107.0, "Premium elektrinis motociklas iš Italijos.", "static/images/energica_eva_ribelle.jpg", "Electric"),
    ("Harley-Davidson LiveWire", "Harley-Davidson", 24000, 2021, 78.0, "Harley elektrinė revoliucija – greitas ir stilingas.", "static/images/livewire.jpg", "Electric"),
    ("Sondors Metacycle", "Sondors", 7200, 2022, 14.0, "Prieinamas miesto elektrinis motociklas.", "static/images/sondors_metacycle.jpg", "Electric"),
]

with app.app_context():
    kategorijos = {k.pavadinimas: k.id for k in Kategorija.query.all()}

    for m in motociklai:
        if not Motociklas.query.filter_by(modelis=m[0]).first():
            db.session.add(Motociklas(
                modelis=m[0],
                gamintojas=m[1],
                kaina=m[2],
                pagaminimo_metai=m[3],
                galia_kw=m[4],
                aprasymas=m[5],
                nuotrauka_url=m[6],
                kategorija_id=kategorijos.get(m[7])
            ))

    db.session.commit()
    print("✅ Visi papildomi motociklai sėkmingai pridėti!")