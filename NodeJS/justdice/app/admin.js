import db from "./connect.js";
import SeedDetail from "./seed_detail.js";
import User from "./users.js";
import pool from './connection_pool.js';

const Admin = {};

Admin.initialize = function(app) {

    app.get('/admin/users', function(request, response) {
        User.page(1, function(data) {
            response.render("users", { users: data });
        });
    });

    app.get('/users', async (req, res) => {
        try {
            // Lấy kết nối từ pool
            const connection = await pool.getConnection();

            // Thực hiện truy vấn
            const [rows] = await connection.query('SELECT id, username, points, gid FROM users');

            // Giải phóng kết nối về pool 
            connection.release();

            console.log('Data from users:', rows);
            res.render('users', { users: rows }); // Sửa lại thành 'users' thay vì 'index'
        } catch (error) {
            console.error('Error executing query:', error);
            res.status(500).send('Internal Server Error'); // Trả về lỗi server
        }
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
