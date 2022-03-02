from urllib import request
from flask import Blueprint, render_template, redirect, url_for, request, flash
from . import db
from .models import User
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import re

auth = Blueprint("auth", __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, password):
                flash('Logged In', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Password is Incorrect', category='error')
        else:
            flash('email does not exist', category='error')

    return render_template('login.html', user=current_user)

@auth.route('/sign-up', methods=['GET', 'POST'])
def signUp():
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

    if request.method == 'POST':
        email = request.form.get("email")
        username = request.form.get("username")
        passwordOne = request.form.get("password1")
        passwordTwo = request.form.get("password2")
        admin = request.form.get('admin')

        email_exists =User.query.filter_by(email=email).first()
        username_exists = User.query.filter_by(username=username).first()

        if email_exists:
            flash('Email is already in use.', category='error')
        elif not re.fullmatch(regex, email):
            flash('Improper email format', category='error')
        elif username_exists:
            flash('Username is already in use.', category='error')
        elif passwordOne != passwordTwo:
            flash('Passwords don\'t match.', category='error')
        elif len(username) < 2:
            flash('Username is too short.', category='error')
        elif len(passwordOne) < 6:
            flash('Password is too short.', category='error') 
        elif len(email) < 4:
            flash('email is invalid', category='error')
        elif admin == "True": 
            new_user = User(email = email, username=username, password=generate_password_hash(passwordOne, method='sha256'), admin=True)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('User created!')
            return redirect(url_for('views.home'))
        else:
            new_user = User(email = email, username=username, password=generate_password_hash(passwordOne, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('User created!')
            return redirect(url_for('views.home'))

    return render_template('register.html', user=current_user)

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("views.home"))


