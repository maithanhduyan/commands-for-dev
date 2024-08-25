/**
 * client
 */
$(function () {
    $('#randomize').click(function (event) {
        console.log('randomize')
    });

    $('#invest_few').click(function (event) {
        var amount = $("#invest_input").val();
        if (amount.length == 0) return;
        var val = parseFloat(amount);
        if (!isNaN(val)) {
            socket.emit("invest", {amount: amount, gid: getCookie("gambit_guid")});
            $("#invest_input").val("");
        }
    });

    $('#invest_all').click(function (event) {
        socket.emit("invest-all", {gid: getCookie("gambit_guid")});
    })

    $('#setup').submit(function (event) {

        var username = $('#username').val();
        var password = $('#password').val();
        console.log(username,password);
        socket.emit("setup", {gid: getCookie("gambit_guid"), username: username, password: password});
        event.preventDefault();
    });


    function set_investment(val) {
        $('.investment').html(parseFloat(val).toFixed(7));
    }

    socket.on("setup-response",function(message){
        if(message.success){
            alert("Setup Successful ");
            $('.unset-account').hide();
            $('#modal-login').modal('hide');
        }else{
            alert("Setup Unsuccessful "+message.message);
        }
    });

    socket.on("update", function (message) {
        $.each(message, function (key, value) {
            switch (key) {
                case "balance":
                    set_bal(value);
                    break;
                case "investment":
                    set_investment(value);
                    break;
                case "bankroll":
                    $('.invest_pct').html(parseFloat(value).toFixed(7));
                    break;

            }
        });
    });
});