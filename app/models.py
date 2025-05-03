from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100))
    usia = db.Column(db.Integer)
    angkatan = db.Column(db.String(10))
    prodi = db.Column(db.String(100))
    domisili = db.Column(db.String(100))
    jenis_kelamin = db.Column(db.String(10))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Gejala(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    kode = db.Column(db.String(10), unique=True)
    deskripsi = db.Column(db.String(255))

class Hipotesis(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    kode = db.Column(db.String(10), unique=True)
    tingkat = db.Column(db.String(100))

class BasisPengetahuan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gejala_id = db.Column(db.Integer, db.ForeignKey('gejala.id'))
    hipotesis_id = db.Column(db.Integer, db.ForeignKey('hipotesis.id'))
    bobot = db.Column(db.Float)  # nilai bobot dari basis pengetahuan

    gejala = db.relationship('Gejala', backref=db.backref('basis_pengetahuan', lazy=True))
    hipotesis = db.relationship('Hipotesis', backref=db.backref('basis_pengetahuan', lazy=True))

class SkalaCF(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(50))  # contoh: "Yakin", "Sangat Yakin"
    nilai = db.Column(db.Float)       # contoh: 0.8, 1.0

class JawabanUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    gejala_id = db.Column(db.Integer, db.ForeignKey('gejala.id'))
    nilai_cf = db.Column(db.Float)

    user = db.relationship('User', backref=db.backref('jawaban', lazy=True))
    gejala = db.relationship('Gejala')

class HasilDiagnosa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    hipotesis_id = db.Column(db.Integer, db.ForeignKey('hipotesis.id'))
    nilai_cf = db.Column(db.Float)
    metode = db.Column(db.String(50))  # backward_chaining / certainty_factor
    tanggal = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship('User')
    hipotesis = db.relationship('Hipotesis')
