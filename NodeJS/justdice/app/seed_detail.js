import db from "./connect.js";
import Seed from "./seed.js";

const SeedDetail = {};

SeedDetail.create = function (user_id, user_gid, callback) {
    db.query(
        'INSERT INTO seed_details (user_id, user_gid, server_seed, client_seed) VALUES (?,?,?,?);',
        [
            user_id,
            user_gid,
            Seed.create_server_seed(),
            Seed.create_client_seed()
        ],
        function (err, rows) {
            if (err) {
                console.log(err);
                throw err;
            }
            console.log(err, rows);
            SeedDetail.find(rows.insertId, callback);
        }
    );
};

SeedDetail.find = function (id, callback) {
    db.query('SELECT * FROM seed_details where id = ?', [id], function (err, rows) {
        if (err) {
            console.log(err);
            callback(err, null);
        } else if (rows.length === 0) {
            console.log("No seed detail by the id:" + id);
            callback(null, null);
        } else {
            callback(null, rows[0]);
        }
    });
};

export default SeedDetail;
