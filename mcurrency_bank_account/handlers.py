from app import socketio, app, db
from flask import Flask, session, request
from flask_socketio import emit, disconnect
from flask_login import current_user
import functools
import models
from decimal import Decimal

def allow_authenticated(f):
    @functools.wraps(f)
    def wrapped(*args, **kwargs):
        if not current_user.is_authenticated:
            disconnect()
        else:
            return f(*args, **kwargs)
    return wrapped

@socketio.on('bank_get_balances', namespace='/bank')
@allow_authenticated
def handle_get_balances():
    app.logger.debug('get_balances.')
    pass

@socketio.on('bank_deposit', namespace='/bank')
@allow_authenticated
def handle_deposit(deposit):
    bank = models.Bank.query.filter_by(user_id=current_user.id).first()
    amount = Decimal(deposit.get('amount'))

    if bank is None:
        bank = models.Bank(currency=deposit.get('currency'), user_id=current_user.id, user=current_user, amount=amount)
        db.session.add(bank)
        db.session.commit()
        return bank.serializer()

    bank.amount += amount
    db.session.commit()
    return bank.serializer()

@socketio.on('bank_withdrawal', namespace='/bank')
@allow_authenticated
def handle_withdrawal():
    pass

@socketio.on('bank_transfer', namespace='/bank')
@allow_authenticated
def handle_transfer():
    pass

@socketio.on('connect', namespace='/bank')
def test_connect():
    if not current_user.is_authenticated:
        return False

    emit('bank_joined', {
         'username': current_user.username, 'id': current_user.id,
         'bank': current_user.banks[0].serializer() if len(current_user.banks) > 0 else { 'amount': 0.00 }
         })

    app.logger.debug('Client connected.')

@socketio.on('disconnect', namespace='/bank')
def test_disconnect():
    app.logger.debug('Client disconnected.')
