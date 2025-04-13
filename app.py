from flask import Flask, render_template, request, redirect, url_for
from models import db, Motociklas, Kategorija
from sqlalchemy import func

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///katalogas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def pagrindinis_puslapis():
    paieska = request.args.get('search')
    metai_nuo = request.args.get('metai_nuo')
    metai_iki = request.args.get('metai_iki')
    kaina_nuo = request.args.get('kaina_nuo')
    kaina_iki = request.args.get('kaina_iki')

    uzklausa = db.session.query(Motociklas).join(Kategorija)

    if paieska:
        uzklausa = uzklausa.filter(
            (Motociklas.modelis.ilike(f'%{paieska}%')) |
            (Motociklas.gamintojas.ilike(f'%{paieska}%')) |
            (Kategorija.pavadinimas.ilike(f'%{paieska}%'))
        )

    if metai_nuo:
        uzklausa = uzklausa.filter(Motociklas.pagaminimo_metai >= int(metai_nuo))
    if metai_iki:
        uzklausa = uzklausa.filter(Motociklas.pagaminimo_metai <= int(metai_iki))

    if kaina_nuo:
        uzklausa = uzklausa.filter(Motociklas.kaina >= float(kaina_nuo))
    if kaina_iki:
        uzklausa = uzklausa.filter(Motociklas.kaina <= float(kaina_iki))

    motociklai = uzklausa.all()
    return render_template(
        'index.html',
        motociklai=motociklai,
        paieska=paieska,
        metai_nuo=metai_nuo,
        metai_iki=metai_iki,
        kaina_nuo=kaina_nuo,
        kaina_iki=kaina_iki
    )

@app.route('/prideti', methods=['GET', 'POST'])
def prideti_motocikla():
    if request.method == 'POST':
        naujas = Motociklas(
            modelis=request.form['modelis'],
            kaina=float(request.form['kaina']),
            pagaminimo_metai=int(request.form['metai']),
            gamintojas=request.form['gamintojas'],
            galia_kw=float(request.form['galia']),
            aprasymas=request.form['aprasymas'],
            nuotrauka_url=request.form['nuotrauka_url'],
            kategorija_id=int(request.form['kategorija_id'])
        )
        db.session.add(naujas)
        db.session.commit()
        return redirect(url_for('pagrindinis_puslapis'))
    kategorijos = Kategorija.query.all()
    return render_template('prideti.html', kategorijos=kategorijos)

@app.route('/redaguoti/<int:id>', methods=['GET', 'POST'])
def redaguoti_motocikla(id):
    motociklas = Motociklas.query.get_or_404(id)
    if request.method == 'POST':
        motociklas.modelis = request.form['modelis']
        motociklas.kaina = float(request.form['kaina'])
        motociklas.pagaminimo_metai = int(request.form['metai'])
        motociklas.gamintojas = request.form['gamintojas']
        motociklas.galia_kw = float(request.form['galia'])
        motociklas.aprasymas = request.form['aprasymas']
        motociklas.nuotrauka_url = request.form['nuotrauka_url']
        motociklas.kategorija_id = int(request.form['kategorija_id'])
        db.session.commit()
        return redirect(url_for('pagrindinis_puslapis'))
    kategorijos = Kategorija.query.all()
    return render_template('redaguoti.html', motociklas=motociklas, kategorijos=kategorijos)

@app.route('/istrinti/<int:id>', methods=['POST'])
def istrinti_motocikla(id):
    motociklas = Motociklas.query.get_or_404(id)
    db.session.delete(motociklas)
    db.session.commit()
    return redirect(url_for('pagrindinis_puslapis'))

@app.route('/statistika')
def statistika():
    rezultatai = db.session.query(
        Kategorija.pavadinimas,
        func.count(Motociklas.id),
        func.avg(Motociklas.kaina)
    ).join(Motociklas).group_by(Kategorija.pavadinimas).all()
    return render_template('statistika.html', statistika=rezultatai)

if __name__ == '__main__':
    app.run(debug=True)