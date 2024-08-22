import db from "./connect.js";
import SeedDetail from "./seed_detail.js";
import User from "./users.js";

const Admin = {};

Admin.initialize = function(app) {

    app.get('/admin/users', function(request, response) {
        User.page(1, function(data) {
            response.render("users", { data: data });
        });
    });

    app.post('/admin/user/edit', function(request, response) {
        const sql = `UPDATE users SET ${request.body.name} = ? WHERE ID = ?`;
        db.query(sql, [request.body.value, request.body.pk], function(err) {
            if (!err) {
                response.json({ success: true });
            } else {
                console.log(err);
                response.status(400).json("Cannot Update");
            }
        });
    });
};

export default Admin;
