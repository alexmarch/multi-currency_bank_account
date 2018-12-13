from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import current_user

import models

bp = Blueprint('dashboard', __name__)

@bp.route('/', methods=['GET'])
def index():
    return render_template('dashboard.html')


@bp.route('/bank/deposit', methods=['GET'])
def deposit():
    return render_template('bank/deposit.html')


@bp.route('/bank/withdraw', methods=['GET'])
def withdraw():
    if len(current_user.banks) == 0:
        flash('Please create first deposit before.','warning')
        return redirect(url_for('dashboard.deposit'))
    bank = current_user.banks[0]
    return render_template('bank/withdraw.html', amount = bank.amount, currency = bank.currency)


@bp.route('/bank/transfer', methods=['GET'])
def transfer():
    return render_template('bank/transfer.html')
