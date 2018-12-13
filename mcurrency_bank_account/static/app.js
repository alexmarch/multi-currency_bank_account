/**
 * Demo application bank client
 */
(function() {
    var socket = io.connect('http://' + document.domain + ':' + location.port + '/bank');
    window.user = {
        profile: {}
    };
    var update_balance = function(amount, currency) {
        var $amount = document.getElementById('amount');
        $amount.innerText = (currency ? '(' + currency + ') ' : '') + (amount ? String(amount) : '0.00') + '$';
    };

    // Socket.IO Handlers
    socket.on('connect', function(args) {
        console.log('connect');
        socket.emit('bank_get_balances');
    });

    socket.on('bank_get_balances', function(balance) {
        update_balance(balance.amount, balance.currency);
    });

    socket.on('bank_joined', function(profile) {
        window.user.profile = profile;
        update_balance(profile.bank.amount, profile.bank.currency);
    });

    // Forms submit handlers
    window.onWithdrawSubmit = function(event) {
        event.preventDefault();

        return false;
    };
    window.onDepositSubmit = function(event) {
        event.preventDefault();
        amount = parseFloat(event.target[0].value);
        currency = event.target[1].value;

        if (!isNaN(amount) || amount <= 0) {
            deposit = { amount: amount, currency: currency };

            socket.emit('bank_deposit', deposit, function(data) {
                update_balance(data.amount, data.currency);
                event.target.reset();
                $.notify('Bank deposit success now your currency (' + data.currency + ')', { position: 'right bottom', className: 'success'});
            });
        } else {
            $.notify('Invalid amount value.', { position: 'right bottom', className: 'error' });
        }
        return false;
    };
})();