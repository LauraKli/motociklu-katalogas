# 🏍️ Motociklų katalogas (Flask + SQLite)

Tai yra mokomasis Flask projektas – motociklų katalogas, leidžiantis peržiūrėti, filtruoti, pridėti, redaguoti ir ištrinti motociklų įrašus.

---

##  Vaizdinė informacija

Projektas rodo motociklų nuotraukas, kurios saugomos kataloge `static/images/`.

✅ Nuotraukų pavadinimai turi sutapti su tais, kurie įrašyti į duomenų bazę (pvz. `yamaha_mt07.jpg`, `bmw_r1250rt.jpg`).

---

## 📂 Projekto struktūra

```
motociklu-katalogas/
├── instance/
├── static/
│   ├── images/
│   └── style.css
├── templates/
├── app.py
├── db_init.py
├── katalogas.db
├── models.py
├── papildyk_db.py
├── patikrink_nuotraukas.py
└── README_LT.md          
```

---

## ✅ Funkcionalumas

-  Paieška pagal modelį, gamintoją ir kategoriją;
-  Filtrai pagal kainą ir pagaminimo metus;
- Naujo motociklo pridėjimas;
- Esamo įrašo redagavimas;
- Įrašo ištrynimas;
- Statistika: kiekvienos kategorijos vidutinė kaina ir kiekis;
- Kiekvienas įrašas turi nuotrauką ir aprašymą;
- Fono paveikslėlis yra pridėtas.

---

## Paleidimo instrukcija

1. Atsisiųskite arba klonuokite šį projektą iš GitHub:

```
git clone https://github.com/TAVO_VARDAS/motociklu-katalogas.git
cd motociklu-katalogas
```

2. Aktyvuokite virtualią aplinką (jei norit) ir įdiekit reikalingus modulius:

```
pip install flask flask_sqlalchemy
```

3. Paleiskite programą:

```
python app.py
```

4. Atidarykite naršyklę ir įveskite:

```
http://127.0.0.1:5000
```

## ℹ️ Pastabos

- Jei nuotraukos nerodomos – galima patikrinkti ar jos tikrai yra `static/images/` kataloge.
- Jei norėsite papildyti duomenų bazę, galit paleisti `papildyk_db.py`:

```
python papildyk_db.py
```

```

---

Projektas sukurtas mokymosi tikslais. Tema pasirinkta pagal asmeninį pomėgį – motociklus. 🧡
