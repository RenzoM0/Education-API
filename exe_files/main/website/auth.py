from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, logout_user, login_required, current_user
from sqlalchemy.sql.expression import true
from .models import Chat
from .models import Rubric


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/admin', methods=['GET', 'POST'])
@login_required
def admin():
    
        if current_user.admin:
            chats = Chat.query.all()
            rubrics = Rubric.query.all()
            if request.method == 'POST':
                course = request.form.get('course')
                instruction = request.form.get('instruction')
            
                new_rubric = Rubric(course=course,rubric_instruction=instruction)
                db.session.add(new_rubric)
                db.session.commit()
            
            return render_template("admin.html", user=current_user, chats=chats, rubrics=rubrics)
        else:
            flash('You do not have permission to access this page.', category='error')
            return redirect(url_for('views.home'))

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        user = User.query.filter_by(email=email).first()
        
        if user:
            flash('Email already exists.', category='error')
            
        elif len(name) < 3:
            flash("Name must be at least 3 characters long", category='error')
            
        elif len(email) < 4:
            flash("Email must be greater than 3 characters.", category='error')
            
        elif password1 != password2:
            flash("Passwords do not match", category='error')
            
        elif len(password1) < 7:
            flash("Password must be at least 7 characters long", category='error')
            
        else:
            new_user = User(email=email, name=name, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash("Registration successful", category='success')
            return redirect(url_for('views.home'))
        
    return render_template("register.html", user=current_user)