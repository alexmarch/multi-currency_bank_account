from flask import Blueprint, g, request, render_template, url_for, flash, redirect
from flask_login import login_user, logout_user, login_required
import models
from app import db

bp = Blueprint('auth', __name__)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('auth/login.html')
    else:
        user = models.User.query.filter_by(username=request.form['username']).first()
        if user is None:
            flash('Invalid username', 'danger')
            return redirect(url_for('auth.login'))

        if not user.is_correct_password(request.form['password']):
            flash('Invalid user password', 'danger')
            return redirect(url_for('auth.login'))

        login_user(user)
        flash('Now you can working with bank account.', 'success')
        return redirect(url_for('dashboard.index'))

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('auth/register.html')
    else:
        user = models.User(request.form['username'], request.form['password'])
        db.session.add(user)
        db.session.commit()
        flash('User successfully registered.', 'success')
        return redirect(url_for('auth.login'))

@bp.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('dashboard.index'))
