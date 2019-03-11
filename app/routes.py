from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required

from app import app, db
from app.forms import LoginForm
from app.forms import RegistrationForm, GejalaForm, PenyakitForm
from app.models import User, Gejala, Penyakit


@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('dashboard.html', title='Home')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
        # next_page = request.args.get('next')
        # if not next_page or url_parse(next_page).netloc != '':
        #     next_page = url_for('index')
        # return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/gejala')
def view_gejala():
    models = Gejala.query.all()
    print(models)
    return render_template('gejala/view.html', title='View Gejala', models=models)


@app.route('/gejala/create', methods=['GET', 'POST'])
def create_gejala():
    form = GejalaForm()
    if form.validate_on_submit():
        gejala = Gejala(nama_gejala=form.nama_gejala.data)
        db.session.add(gejala)
        db.session.commit()
        flash('Data berhasil dimasukkan')
        return redirect(url_for('view_gejala'))
    return render_template('gejala/create.html', title='View Gejala', form=form)


@app.route('/gejala/update/<int:id_gejala>', methods=['GET', 'POST'])
def update_gejala(id_gejala):
    form = GejalaForm()
    gejala = Gejala.query.filter_by(id_gejala=id_gejala).first()
    if form.validate_on_submit():
        gejala.nama_gejala = form.nama_gejala.data
        db.session.commit()
        return redirect(url_for('view_gejala'))
    return render_template('gejala/update.html', title='Update Gejala', gejala=gejala, form=form)


@app.route('/gejala/delete/<int:id_gejala>', methods=['GET', 'POST'])
def delete_gejala(id_gejala):
    gejala = Gejala.query.filter_by(id_gejala=id_gejala).first()
    db.session.delete(gejala)
    db.session.commit()
    return redirect(url_for('view_gejala'))


@app.route('/penyakit')
def view_penyakit():
    models = Penyakit.query.all()
    print(models)
    return render_template('penyakit/view.html', title='View Penyakit', models=models)

@app.route('/penyakit/create', methods=['GET', 'POST'])
def create_penyakit():
    form = PenyakitForm()
    if form.validate_on_submit():
        penyakit = Penyakit(nama_penyakit=form.nama_penyakit.data, definisi_penyakit=form.definisi_penyakit.data, penyebab_penyakit=form.penyebab_penyakit.data, pengobatan_penyakit=form.pengobatan_penyakit.data, pencegahan_penyakit=form.pencegahan_penyakit.data, komplikasi_penyakit=form.komplikasi_penyakit.data)
        db.session.add(penyakit)
        db.session.commit()
        flash('Data berhasil dimasukkan')
        return redirect(url_for('view_penyakit'))
    return render_template('penyakit/create.html', title='View Penyakit', form=form)


@app.route('/penyakit/update/<int:id_penyakit>', methods=['GET', 'POST'])
def update_penyakit(id_penyakit):
    form = PenyakitForm()
    penyakit = Penyakit.query.filter_by(id_penyakit=id_penyakit).first()
    if form.validate_on_submit():
        penyakit.nama_penyakit = form.nama_penyakit.data
        penyakit.definisi_penyakit = form.definisi_penyakit.data
        penyakit.penyebab_penyakit = form.penyebab_penyakit.data
        penyakit.pengobatan_penyakit = form.pengobatan_penyakit.data
        penyakit.pencegahan_penyakit = form.pencegahan_penyakit.data
        penyakit.komplikasi_penyakit = form.komplikasi_penyakit.data
        db.session.commit()
        return redirect(url_for('view_penyakit'))
    return render_template('penyakit/update.html', title='Update Penyakit', penyakit=penyakit, form=form)

@app.route('/penyakit/delete/<int:id_penyakit>', methods=['GET', 'POST'])
def delete_penyakit(id_penyakit):
    penyakit = Penyakit.query.filter_by(id_penyakit=id_penyakit).first()
    db.session.delete(penyakit)
    db.session.commit()
    return redirect(url_for('view_penyakit'))

@app.route('/penyakit/detail/<int:id_penyakit>', methods=['GET'])
def detail_penyakit(id_penyakit):
    models = Penyakit.query.filter_by(id_penyakit=id_penyakit).first()
    print(models)
    return render_template('penyakit/detail.html', title='Detail Penyakit', models=models)

