from flask import Blueprint, render_template, request, flash
import re
auth = Blueprint('auth', __name__)

@auth.route('/sign-up', methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        email = request.form.get('email')
        userName = request.form.get('userName')
        password = request.form.get('password1')
        confirmPassword = request.form.get('password2')
    
        if not is_valid_email(email):
            flash('Invalid email format', 'error')
        elif len(userName) < 3:
            flash('Username should be 8 characters long.', 'error')
        elif password != confirmPassword:
            flash('Password doesn\'t match', 'error')
        elif len(password) < 7:
            flash('password should be 8 characters long.', 'error')
        else:
            flash('Account created!', 'success ')
    return render_template("sign_up.html")


# Function to validate email format
def is_valid_email(email):
    if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
        return True
    return False

@auth.route('/login')
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<h1>logout</h1>"