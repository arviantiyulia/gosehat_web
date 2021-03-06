from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login


@login.user_loader
def load_user(id):
    return User.query.filter(User.id_user==int(id)).first()
   
class User(UserMixin, db.Model):
    id_user = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username) 

    def get_id(self):
           return (self.id_user)

class Gejala(db.Model):
    id_gejala = db.Column(db.Integer, primary_key=True)
    nama_gejala = db.Column(db.String(255))
    gejalapenyakit = db.relationship('GejalaPenyakit', backref='gejala', lazy='dynamic')

    def __repr__(self):
        return '<Gejala {}>'.format(self.id_gejala)


class Penyakit(db.Model):
    id_penyakit = db.Column(db.Integer, primary_key=True)
    nama_penyakit = db.Column(db.String(255))
    definisi_penyakit = db.Column(db.String(255))
    penyebab_penyakit = db.Column(db.String(255))
    pengobatan_penyakit = db.Column(db.String(255))
    pencegahan_penyakit = db.Column(db.String(255))
    komplikasi_penyakit = db.Column(db.String(255))
    gejalapenyakit = db.relationship('GejalaPenyakit', backref='penyakit', lazy='dynamic')

    def __repr__(self):
        return '<Penyakit {}>'.format(self.id_penyakit)


class GejalaPenyakit(db.Model):
    id_gejala_penyakit = db.Column(db.Integer, primary_key=True)
    bobot = db.Column(db.Float)
    id_gejala = db.Column(db.Integer, db.ForeignKey('gejala.id_gejala'))
    id_penyakit = db.Column(db.Integer, db.ForeignKey('penyakit.id_penyakit'))

    def __repr__(self):
        return '<GejalaPenyakit {}>'.format(self.id_gejala_penyakit)

class History(db.Model):
    id_history = db.Column(db.Integer, primary_key=True)
    input_user = db.Column(db.String(255))
    output_sistem = db.Column(db.String(255))
    user_id = db.Column(db.String(255))
    name_user = db.Column(db.String(255))
    time = db.Column(db.DateTime(6))
    # id_penyakit = db.Column(db.Integer(32))
    id_penyakit = db.Column(db.Integer, db.ForeignKey('penyakit.id_penyakit'))

    def __repr__(self):
        return '<History {}>'.format(self.id_history)

