from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, Required, Email, EqualTo
from app.models import User, Gejala, Penyakit

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[Required()])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[Required()])
    email = StringField('Email', validators=[Required(), Email()])
    password = PasswordField('Password', validators=[Required()])
    password2 = PasswordField(
        'Repeat Password', validators=[Required(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

class GejalaForm(FlaskForm):
    nama_gejala = StringField('Nama Gejala', validators=[Required()])
    submit = SubmitField('Simpan')


class PenyakitForm(FlaskForm):
    nama_penyakit = StringField('Nama Penyakit', validators=[Required()])
    definisi_penyakit = StringField('Definisi Penyakit', validators=[Required()])
    penyebab_penyakit = StringField('Penyebab Penyakit') 
    pengobatan_penyakit = StringField('Pengobatan Penyakit')
    pencegahan_penyakit = StringField('Pencegahan Penyakit')
    komplikasi_penyakit = StringField('Komplikasi Penyakit')
    submit = SubmitField('Simpan')

class RuleForm(FlaskForm):
    bobot = FloatField('Bobot', validators=[Required()])
    id_penyakit = QuerySelectField(query_factory=lambda: Penyakit.query.all())
