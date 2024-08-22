import db from "./connect.js";
import SeedDetail from "./seed_detail.js";
import User from "./users.js";

const Bet = {};

Bet.create = function (options, callback) {
    db.query("START TRANSACTION");
    db.query(
        'INSERT INTO bets (user_id,seed_detail_id,roll,won,bet,payout,profit,chance,target,lucky,nonce) VALUES (?,?,?,?,?,?,?,?,?,?,?);',
        options,
        function (err, rows) {
            if (err) {
                console.log(err);
                db.query("ROLLBACK");
                throw err;
            } else {
                User.user_point_add(options[0], options[6], function (user_err) {
                    User.banker_point_add(-options[6], function () {
                        db.query("COMMIT", function (err) {
                            if (err) callback(null, err);
                            else callback(rows.insertId);
                        });
                    });
                });
            }
        }
    );
};

Bet.get_next_nonce = function (options, callback) {
    db.query('SELECT count(id) FROM bets WHERE seed_detail_id = ? AND user_id = ?', options,
        function (err, rows) {
            callback(rows[0]["count(id)"]);
        }
    );
};

Bet.get_last_n_bets_by_id = function (n, id, callback) {
    db.query("SELECT * FROM bets WHERE user_id = ? ORDER BY id DESC LIMIT ? ", [id, n], function (err, rows) {
        callback(err, rows);
    });
};

Bet.get_last_n_bets = function (n, callback) {
    db.query("SELECT * FROM bets ORDER BY id DESC LIMIT ? ", [n], function (err, rows) {
        callback(err, rows);
    });
};

Bet.find = function (id, callback) {
    db.query('SELECT * FROM bets WHERE id = ?', [id], function (err, rows) {
        if (err) {
            console.log(err);
            callback(err, null);
        } else if (rows.length === 0) {
            console.log("No bet by the id:" + id);
            callback(err, null);
        } else {
            callback(null, rows[0]);
        }
    });
};

export default Bet;
