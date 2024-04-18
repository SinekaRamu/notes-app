from flask import Blueprint, render_template, request, flash, redirect, url_for
import re
from . import db
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)

@auth.route('/sign-up', methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        email = request.form.get('email')
        userName = request.form.get('userName')
        password = request.form.get('password1')
        confirmPassword = request.form.get('password2')
    
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already registered', 'error')
        elif not is_valid_email(email):
            flash('Invalid email format', 'error')
        elif len(userName) < 3:
            flash('Username should be 8 characters long.', 'error')
        elif password != confirmPassword:
            flash('Password doesn\'t match', 'error')
        elif len(password) < 7:
            flash('password should be 8 characters long.', 'error')
        else:
            new_user = User(email=email, user_name= userName, password=generate_password_hash(password, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!', 'success ')
            return redirect(url_for('views.home'))
    return render_template("sign_up.html")


# Function to validate email format
def is_valid_email(email):
    if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
        return True
    return False

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in Successfully!', 'success')
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect Password, try again?', 'error')
        else:
            flash('User not found', 'error')

    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<h1>logout</h1>"