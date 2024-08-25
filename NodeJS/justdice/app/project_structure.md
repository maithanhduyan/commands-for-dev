# You are an intelligent programming assistant.
# This is nodejs project

# Directory tree of C:\Users\tiach\Downloads\commands-for-dev\NodeJS\justdice\app

├── app/
│   ├── .dockerignore
│   ├── .env
│   ├── .env.example
│   ├── admin.js
│   ├── analytic.py
│   ├── api.js
│   ├── app.js
│   ├── bet.js
│   ├── cache.js
│   ├── chat.js
│   ├── client.js
│   ├── connect.js
│   ├── connection_pool.js
│   ├── dice.js
│   ├── Dockerfile
│   ├── error_code.js
│   ├── invest.js
│   ├── justdice.sql
│   ├── middleware.js
│   ├── package-lock.json
│   ├── package.json
│   ├── redis.js
│   ├── seed.js
│   ├── seed_detail.js
│   └── users.js
│   ├── .vscode/
│   │   ├── launch.json
│   │   └── settings.json
│   ├── public/
│   │   ├── admin.jpg
│   │   ├── bootstrap-responsive.css
│   │   ├── bootstrap-responsive.min.css
│   │   ├── bootstrap-theme.css
│   │   ├── bootstrap-theme.min.css
│   │   ├── bootstrap.css
│   │   ├── bootstrap.min.css
│   │   ├── bootstrap.min.js
│   │   ├── cour.ttf
│   │   ├── docs.css
│   │   ├── favicon.ico
│   │   ├── gambit.css
│   │   ├── gambit.js
│   │   ├── index.html
│   │   ├── jquery.min.js
│   │   ├── login.css
│   │   └── login.html
│   ├── views/
│   │   ├── bet.ejs
│   │   ├── index.ejs
│   │   └── users.ejs
# Content of .js and .ejs files in C:\Users\tiach\Downloads\commands-for-dev\NodeJS\justdice\app

## C:\Users\tiach\Downloads\commands-for-dev\NodeJS\justdice\app\admin.js
```
import db from "./connect.js";
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

```

## C:\Users\tiach\Downloads\commands-for-dev\NodeJS\justdice\app\api.js
```

const ServerAPI = {};

ServerAPI.initialize = function (app) {
    const version = "v1";

    // http://localhost:3000/api/gid
    app.get('/api/gid', (req, res) => {
        const gid = req.cookies.gambit_guid;
        res.json({ gid: gid });
    });
}

export default ServerAPI;
```

## C:\Users\tiach\Downloads\commands-for-dev\NodeJS\justdice\app\app.js
```
import express from 'express';
import Seed from './seed.js';
import Bet from './bet.js';
import User from './users.js';
import SeedDetail from './seed_detail.js'; // Thiết lập cổng cho ứng dụng.js';
import err_code from "./error_code.js";
import Chat from "./chat.js";
import Pool from "./client.js";
import Invest from "./invest.js";
import crypto from 'crypto';
import Admin from './admin.js';
import { Server as SocketIOServer } from 'socket.io';
import { createServer } from 'http';
import cookieParser from 'cookie-parser';
import morgan from 'morgan';
import methodOverride from 'method-override'; // Import method-override
import dotenv from 'dotenv';
import ServerAPI from './api.js';
import { v4 as uuidv4 } from 'uuid';
import { setCookieMiddleware } from './middleware.js' ;


dotenv.config();

var ipaddr = process.env.SERVER_NAME || "127.0.0.1";
var port = process.env.SERVER_PORT || 3000;

const app = express();
const httpServer = createServer(app);
const io = new SocketIOServer(httpServer);


app.set('port', process.env.PORT || port);

// Thiết lập các middleware
app.use(morgan('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(cookieParser()); // Sử dụng cookie-parser để phân tích cookies
app.use(methodOverride('_method')); // Sử dụng methodOverride để hỗ trợ PUT/DELETE trong form HTML
// app.use(setCookieMiddleware);

// Cấu hình thư mục public để phục vụ các tệp tĩnh
app.use(express.static('public'));

// Thiết lập EJS
app.set('view engine', 'ejs');
app.set('views', './views');

process.on('uncaughtException', function (err) {
    console.log(err);
});

// development only
// Middleware ghi log chi tiết chỉ trong môi trường development
if (app.get('env') === 'development') {
    app.use(morgan('dev')); // Sử dụng morgan để ghi log các request trong môi trường phát triển

    // Middleware xử lý lỗi cho môi trường development
    app.use((err, req, res, next) => {
        console.error(err.stack);
        res.status(500).send({
            message: err.message,
            error: err // Hiển thị chi tiết lỗi trong response
        });
    });
}


// Tạo route cho trang chủ "/"
app.get('/', (req, res) => {
    const appCookieName = 'gambit_guid';
    // Setting a cookie
    if (!req.cookies[appCookieName]) {
        let gid = uuidv4();
        res.cookie(appCookieName, gid, {
            maxAge: 900000,
            httpOnly: false, //  True: Chỉ cho phép truy cập cookie từ server
            secure: process.env.NODE_ENV === 'production', // Chỉ sử dụng cookie qua HTTPS khi ở môi trường production
            sameStie: 'None',
        });
        User.create(gid, function (err, success) {
            console.log(`Tạo gid: ${gid} mới và points: ${points}`)
        })
    }
    res.render('index');
});

// Initialize Admin
Admin.initialize(app);

// API Route
ServerAPI.initialize(app);

// Socket.IO 
io.on('connection', (socket) => {
    console.log('A user connected');

    socket.on('message', (msg) => {
        console.log('Message received:', msg);
    });

    socket.on('disconnect', () => {
        console.log('User disconnected');
    });
});

app.post("/login", function (req, res) {
    User.find_by_name(req.body.username, function (err, data) {
        if (err) {
            res.redirect("/login.html?err=1&username=" + req.body.username);
        } else {
            User.login(req.body.username, req.body.password, function (logged_in) {
                if (logged_in) {
                    res.cookie('gambit_guid', data.gid);
                    res.redirect("/");
                } else {
                    res.redirect("/login.html?err=1&username=" + req.body.username);
                }
            });
        }
    });
    console.log(req.body.username);
    console.log(req.body.password);
});

app.get('/login/:gid', function (request, response) {
    User.find_by_gid(request.params.gid, function (err, data) {
        if (!err) response.cookie('gambit_guid', request.params.gid);
        response.redirect("/");
    });
});

app.get('/bet/:betid', function (request, response) {
    Bet.find(request.params.betid, function (err, result) {
        if (result) {
            SeedDetail.find(result.seed_detail_id, function (err, seed_data) {
                console.log(seed_data, err);
                if (!err) {
                    seed_data["server_hash"] = crypto.createHash('sha256').update(seed_data.server_seed).digest("hex");
                    response.render("bet", { result: result, seed: seed_data });
                }
            });
        }
    });
});

// Initialize chat module with Socket.IO
Chat.initialize(io);

io.sockets.on('connection', function (socket) {
    Invest.initialize(socket);
    User.initialize(socket);
    socket.on('message', function (message) {
        switch (message.action) {
            case "new-bet":
                process_new_bet(message, socket);
                break;
            case "randomize-seed":
                process_randomize_seed(message);
                break;
            case "username":
                process_username(socket, message);
                break;
        }
    });

    socket.on('chat', function (message) {
        User.find_by_gid(message.gid, function (err, data) {
            console.log(data);
            if (message.message.substring(0, 3) === "/pm") {
                const pm = message.message.split(" ");
                const to = pm[1];
                if (!pm[1]) socket.emit("error", handle_error(5));
                if (!pm[2]) socket.emit("error", handle_error(6));
                pm.splice(0, 2);
                const text = pm.join(' ');
                User.is_present_by_name(to, function (err, result) {
                    if (result) {
                        Chat.addMessage(data.username, to, text);
                    } else {
                        socket.emit("error", handle_error(4));
                    }
                });
            } else {
                Chat.addMessage(data.username, null, message.message);
            }
        });
    });

    function send_last_bets(socket, id) {
        Bet.get_last_n_bets(30, function (err, rows) {
            socket.emit("message", { action: "old_bet", bets: rows });
        });
        Bet.get_last_n_bets_by_id(30, id, function (err1, rows1) {
            socket.emit("message", { action: "my_old_bet", bets: rows1 });
        });
    }

    socket.on('justnow', function (message) {
        console.log(message);
        if (!message.gid) {
            console.log(`error`);
            socket.emit("error", handle_error(1));
        } else {
            User.find_by_gid(message.gid, function (err, data) {
                if (err) {
                    socket.emit("error", handle_error(err.code));
                } else {
                    if (data.seed_detail_id === 0) {
                        SeedDetail.create(data.id, data.gid, function (err, seed_data) {
                            User.set_new_seed(data.gid, seed_data.id, function (user_update) {
                                if (user_update.changedRows === 1) {
                                    message = {
                                        "action": "seed_data",
                                        "ssh": Seed.get_server_hash_by_seed(seed_data.server_seed),
                                        "cs": seed_data.client_seed,
                                        "nonce": 1,
                                        "balance": data.points,
                                        "name": data.username,
                                        "id": data.id,
                                        "gid": data.gid
                                    };
                                    socket.emit("message", message);
                                    send_last_bets(socket, data.id);
                                    if (data.username)
                                        Pool.add_client(socket, message.name, data.gid);
                                }
                            });
                        });
                    } else {
                        SeedDetail.find(data.seed_detail_id, function (err, seed_data) {
                            message = {
                                "action": "seed_data",
                                "ssh": Seed.get_server_hash_by_seed(seed_data.server_seed),
                                "cs": seed_data.client_seed,
                                "nonce": 1,
                                "balance": data.points,
                                "name": data.username,
                                "id": data.id,
                                "gid": data.gid
                            };
                            message["setup"] = (data.username && data.password) ? 1 : 0;
                            if (data.username)
                                Pool.add_client(socket, message.name, data.gid);
                            socket.emit("message", message);
                            send_last_bets(socket, data.id);
                            Invest.emit_investment(data.id, socket);
                        });
                    }
                }
            });
        }
    });

});

function handle_error(err) {
    return err_code[err];
}

function process_new_bet(message, socket) {
    User.bet(message, function (bet_results, err) {
        if (err) {
            socket.emit("error", err);
        } else {
            Bet.find(bet_results["bet_result_data"], function (err, bet_data) {
                if (bet_data) {
                    bet_data["action"] = "new_bet";
                    io.sockets.emit("message", bet_data);
                    bet_data["action"] = "my_bet";
                    socket.emit("message", bet_data);
                    socket.emit("balance", bet_results["user_balance"]);
                }
            });
        }
    });
}

function process_username(socket, message) {
    User.is_present_by_name(message.name, function (err, result) {
        if (err) {
            console.log("User.is_present_by_name:", err);
        } else {
            if (result) {
                socket.emit("error", handle_error(3));
            } else {
                User.set_name_by_gid(message.gid, message.name, function (err, result) {
                    Pool.add_client(socket, message.name, message.gid);
                    socket.emit("message", { action: 'new_name', name: message.name });
                });
            }
        }
    });
}

function process_randomize_seed(message) {
    // Implement randomize seed logic if needed
}


// Bắt đầu server
httpServer.listen(app.get('port'), ipaddr, () => {
    console.log(`[${Date.now().toString()}][${app.get('env')}]: Server running at http://${ipaddr}:${app.get('port')}/`);
});
```

## C:\Users\tiach\Downloads\commands-for-dev\NodeJS\justdice\app\bet.js
```
import db from "./connect.js";
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

```

## C:\Users\tiach\Downloads\commands-for-dev\NodeJS\justdice\app\cache.js
```
const Cache = {};

export default Cache;

```

## C:\Users\tiach\Downloads\commands-for-dev\NodeJS\justdice\app\chat.js
```
import Pool from "./client.js";

const Chat = {};

let index = 0;
let lastAccessed = 0;

const char_history = {};
let io;

function htmlEscape(str) {
    return String(str)
        .replace(/&/g, '&amp;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#39;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/\//g, '&#x2F');
}

Chat.addMessage = function (from, to, message) {
    message = htmlEscape(message);
    if (to == null) {
        io.sockets.emit("chat", { from: from, message: message, private: false });
    } else {
        Pool.get_client_by_name(to).emit("chat", { from: from, message: message, private: true });
        Pool.get_client_by_name(from).emit("chat", { from: from, message: message, private: true });
    }
}

Chat.initialize = function (server) {
    io = server;
}

export default Chat;

```

## C:\Users\tiach\Downloads\commands-for-dev\NodeJS\justdice\app\client.js
```
import User from './users.js';

const Pool = {};

const client_sockets = {};
const client_sockets_name = {};

Pool.add_client = function (socket, name, gid) {
    client_sockets[gid] = socket;
    client_sockets_name[name] = gid;
};

Pool.del_client = function (gid) {
    delete client_sockets[gid];
    User.find_by_gid(gid, function(err, data) {
        if (data && data.username) {
            delete client_sockets_name[data.username];
        }
    });
};

Pool.get_client = function (gid) {
    return client_sockets[gid];
};

Pool.get_client_by_name = function (name) {
    return client_sockets[client_sockets_name[name]];
};

export default Pool;

```

## C:\Users\tiach\Downloads\commands-for-dev\NodeJS\justdice\app\connect.js
```
import dotenv from 'dotenv';

dotenv.config();

// Truy cập biến môi trường
const dbHost = process.env.DB_HOST;
const dbName = process.env.DB_NAME;
const dbPort = process.env.DB_PORT || 3306;
const dbUser = process.env.DB_USER;
const dbPass = process.env.DB_PASSWORD;

// import mysql from 'mysql2/promise';

// const connectDB = async () => {
//   try {
//     const connection = await mysql.createConnection({
//       host: 'localhost',
//       user: 'admin',
//       password: 'admin@2024', // Thay thế bằng mật khẩu MySQL của bạn
//       database: 'justdice'
//     });

//     console.log('Connected to MySQL Database');
//     return connection;
//   } catch (error) {
//     console.error('Error connecting to MySQL Database:', error);
//     throw error;
//   }
// };
// 

import mysql from 'mysql2';

const connection = mysql.createConnection({
    host: dbHost,
    database: dbName,
    user: dbUser,
    password: dbPass,
});

connection.connect(function(err) {
    if (err) throw err;
    console.log('Connected to the database!');
});

export default connection;



```

## C:\Users\tiach\Downloads\commands-for-dev\NodeJS\justdice\app\connection_pool.js
```
import mysql from 'mysql2/promise'; 
import dotenv from 'dotenv';

dotenv.config();

// Truy cập biến môi trường
const dbHost = process.env.DB_HOST;
const dbName = process.env.DB_NAME;
const dbPort = process.env.DB_PORT || 3306;
const dbUser = process.env.DB_USER;
const dbPass = process.env.DB_PASSWORD;
// Tạo pool kết nối MySQL
const pool = mysql.createPool({
    host: dbHost,
    user: dbUser,
    password: dbPass,
    database: dbName,
    waitForConnections: true,
    connectionLimit: 10, // Giới hạn số lượng kết nối trong pool
    queueLimit: 0
});

export default pool;
```

## C:\Users\tiach\Downloads\commands-for-dev\NodeJS\justdice\app\dice.js
```
const Dice = {};

Dice.get_target = function (chance, roll) {
    
    // Chuyển đổi thành số trước
    chance = parseFloat(chance); 
    
    if (roll === "rhigh") {
        // Áp dụng toFixed sau khi tính toán
        return parseFloat((99.999999 - chance).toFixed(7)); 
    }
    return parseFloat(chance.toFixed(7));
};

Dice.calculate_payout = function (chance) {
    const house_edge = 1;
    return parseFloat((100 - house_edge) / chance).toFixed(7);
};

Dice.calculate_profit = function (chance, bet) {
    return parseFloat((Dice.calculate_payout(chance) - 1) * bet).toFixed(7);
};

export default Dice;

```

## C:\Users\tiach\Downloads\commands-for-dev\NodeJS\justdice\app\error_code.js
```
const err_code = {
    1: {
        error: 1,
        display: "alert",
        type: "danger",
        message: "Kindly delete your cookies and try again"
    },
    2: {
        error: 2,
        display: "alert",
        type: "danger",
        message: "Insufficient balance"
    },
    3: {
        error: 3,
        display: "alert",
        type: "danger",
        message: "Username not available"
    },
    4: {
        error: 4,
        display: "alert",
        type: "danger",
        message: "Specified user not available"
    },
    5: {
        error: 5,
        display: "alert",
        type: "danger",
        message: "Kindly specify a user"
    },
    6: {
        error: 6,
        display: "alert",
        type: "danger",
        message: "Message missing"
    },
    7: {
        error: 7,
        display: "invest-alert",
        type: "danger",
        message: "Insufficient balance"
    }
};

export default err_code;

```

## C:\Users\tiach\Downloads\commands-for-dev\NodeJS\justdice\app\invest.js
```
import User from "./users.js";
import db from "./connect.js";
import err_code from "./error_code.js";

const Invest = {};

Invest.initialize = function (socket) {
    socket.on("invest-all", function (message) {
        User.find_by_gid(message.gid, function (err, user_data) {
            if (user_data.points > 0) {
                Invest.create(user_data.id, user_data.points, function (err, data) {
                    if (err) {
                        console.log("Invest.initialize", err);
                    } else {
                        Invest.get_total_investments(user_data.id, function (err, total) {
                            socket.emit("update", { balance: data.info.points - user_data.points, investment: total });
                        });
                    }
                });
            }
        });
    });

    socket.on("invest", function (message) {
        const amount = parseFloat(message.amount);
        if (!isNaN(amount) && amount > 0) {
            User.find_by_gid(message.gid, function (err, user_data) {
                if (err) {
                    callback(err, null);
                } else {
                    if (amount <= user_data.points) {
                        Invest.create(user_data.id, message.amount, function (err, data) {
                            if (err) {
                                console.log("Invest.initialize", err);
                            } else {
                                Invest.get_total_investments(user_data.id, function (err, total) {
                                    socket.emit("update", { balance: data.info.points - amount, investment: total });
                                });
                            }
                        });
                    } else {
                        socket.emit("error", err_code[7]);
                    }
                }
            });
        }
    });
};

Invest.emit_investment = function (id, socket) {
    Invest.calculate_profit(id, function (err, profit, total, balance) {
        if (!err) socket.emit("update", { investment: total, bankroll: ((profit / balance) * 100).toFixed(7) });
    });
};

Invest.create = function (user, amount, callback) {
    db.query("START TRANSACTION");
    User.find(1, function (err, banker) {
        User.transfer(user, 1, amount, function (err, result) {
            if (err) {
                db.query("ROLLBACK");
                callback(err, null);
            } else {
                db.query("INSERT INTO investments (user_id, invest, bank_balance) VALUES (?, ?, ?)", [user, amount, banker.points + amount],
                    function (err, rows) {
                        if (err) {
                            db.query("ROLLBACK");
                            callback({ err: err, code: -1 }, null);
                        } else {
                            db.query("COMMIT");
                            callback(null, result);
                        }
                    });
            }
        });
    });
};

Invest.create_by_gid = function (user, amount, callback) {
    User.find_by_gid(user, function (err, user_data) {
        if (err) {
            callback(err, null);
        } else {
            Invest.create(user_data.id, amount, callback);
        }
    });
};

Invest.calculate_profit = function (id, callback) {
    Invest.get_all_investments(id, function (err, rows) {
        if (err) {
            callback(err, null);
        } else {
            User.get_balance(1, function (err, current_balance) {
                let profit = 0;
                let total = 0;
                for (let i = 0; i < rows.length; i++) {
                    total += rows[i].invest;
                    profit += (current_balance / rows[i].bank_balance) * rows[i].invest;
                }
                callback(null, profit, total, current_balance);
            });
        }
    });
};

Invest.get_all_investments = function (id, callback) {
    db.query("SELECT * FROM investments WHERE user_id = ? ;", [id], callback);
};

Invest.get_total_investments = function (id, callback) {
    Invest.get_all_investments(id, function (err, data) {
        let total = 0;
        for (let i = 0; i < data.length; i++) {
            total += parseFloat(data[i].invest);
        }
        callback(err, total);
    });
};

export default Invest;

```

## C:\Users\tiach\Downloads\commands-for-dev\NodeJS\justdice\app\middleware.js
```
import crypto from 'crypto';
import Seed from './seed.js';
import User from './users.js';
import { v4 as uuidv4 } from 'uuid';

const appCookieName = 'gambit_guid';

export function setCookieMiddleware(req, res, next) {
    console.log('setCookieMiddleware')
    if (!req.cookies[appCookieName]) {
        // let gid = crypto.createHash('sha256').update(Seed.create_client_seed()).digest('hex');
        let gid = uuidv4();
        let points = 0;
        res.cookie(appCookieName, gid, {
            maxAge: 900000,
            httpOnly: false, //  True: Chỉ cho phép truy cập cookie từ server
            secure: process.env.NODE_ENV === 'production', // Chỉ sử dụng cookie qua HTTPS khi ở môi trường production
            // sameSite: 'strict' // Chỉ gửi cookie cho cùng domain
            sameStie: 'None',
        });
        User.create(gid, function (err, success) {
            console.log(`Tạo gid: ${gid} mới và points: ${points}`)
        })
    }

    next();
}

```

## C:\Users\tiach\Downloads\commands-for-dev\NodeJS\justdice\app\redis.js
```
import redis from "redis";

const client = redis.createClient();

client.on("error", function (err) {
    console.log("Error " + err);
});

export default client;

```

## C:\Users\tiach\Downloads\commands-for-dev\NodeJS\justdice\app\seed.js
```
import crypto from 'crypto';

const Seed = {};

function create_rand_string(length) {
    let text = "";
    const possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789/.,<>?;:[]{}!@#$%^&*()_+-=";

    for (let i = 0; i < length; i++) {
        text += possible.charAt(Math.floor(Math.random() * possible.length));
    }

    return text;
}

Seed.create_server_seed = function () {
    return create_rand_string(64);
}

Seed.create_client_seed = function () {
    return create_rand_string(24);
}

Seed.get_server_hash_by_seed = function (seed) {
    return crypto.createHash('sha256').update(seed).digest("hex");
}

Seed.get_result = function (ssh, ss, cs, sn, nb) {
    let j = sn + nb - 1;
    let gen = "";
    let ss2;
    gen = j + ':' + cs + ':' + j;
    ss2 = j + ':' + ss + ':' + j;
    let hash = crypto.createHmac('sha512', ss2).update(gen).digest('hex');
    let i = 0;
    let roll = -1;

    while (roll === -1) { // Non-reference implementation derived from the 'Fair?' description.
        if (i === 25) {
            let l3 = hash.substring(125, 128);
            let l3p = parseInt(l3, 16);
            roll = l3p / 10000;
        } else {
            let f5 = hash.substring(5 * i, 5 + 5 * i);
            let f5p = parseInt(f5, 16);

            if (f5p < 1000000) {
                roll = f5p / 10000;
            }
            i++;
        }
    }
    return roll;
}

export default Seed;

```

## C:\Users\tiach\Downloads\commands-for-dev\NodeJS\justdice\app\seed_detail.js
```
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

```

## C:\Users\tiach\Downloads\commands-for-dev\NodeJS\justdice\app\users.js
```
import db from "./connect.js";
import Bet from './bet.js';
import Dice from './dice.js';
import SeedDetail from './seed_detail.js';
import Seed from './seed.js';
import crypto from 'crypto';
import pool from "./connection_pool.js";

const User = {};

User.initialize = function (socket) {
    socket.on("setup", function (message) {
        console.log(message);
        User.is_present_by_name(message.username, function (err, result, user) {
            if (err) {

            }
            else if ((!result) || (result && user.gid == message.gid)) {
                User.setup_user_by(message, function (err, response) {
                    if (err) {
                        console.log("on setup:", err);
                        socket.emit("setup-response", { success: false });
                    } else {
                        socket.emit("setup-response", { success: true });
                    }
                });
            } else {
                socket.emit("setup-response", { success: false, message: "Name Already Taken" });
            }
        });
    });
}

User.login_by_gid = function (gid, callback) {
    User.find_by_gid(gid, function (err, rows) {
        if (!err && rows.length == 1)
            callback(true);
        else {
            console.log(err, rows);
            callback(false);
        }
    });
};

User.find = function (id, callback) {
    db.query('SELECT * FROM users where id = ?', [id], function (err, rows) {
        if (err) {
            console.log(err);
            callback(err, null);
        } else if (rows.length === 0) {
            console.log("No user by the id:" + id);
        } else {
            callback(err, rows[0]);
        }
    });
};

User.find_by_gid = function (gid, callback) {
    db.query('SELECT * FROM users where gid = ?', [gid], function (err, rows) {
        if (err) {
            console.log(err);
            throw err;
        }
        if (rows.length === 0) {
            console.log("No user by the gid:" + gid);
            callback({ err: "Gid Not Found", code: 1 }, null);
        } else {
            callback(null, rows[0]);
        }
    });
};

User.set_new_seed = function (gid, seed_detail_id, callback) {
    db.query('UPDATE users set seed_detail_id = ? where gid = ? ', [seed_detail_id, gid], function (err, rows) {
        if (err) {
            console.log(err);
            throw err;
        } else {
            callback(rows);
        }
    });
};

User.bet = function (message, callback) {
    User.find_by_gid(message.gid, function (err, data) {
        if (parseFloat(data.points) < message.bet) {
            callback(null, { err: 2, message: "Insufficient Balance in:User.bet" });
        } else {
            Bet.get_next_nonce([data.seed_detail_id, data.id], function (nonce_data) {
                nonce_data++;
                SeedDetail.find(data.seed_detail_id, function (err, seed_data) {
                    const roll = (message.roll === "rhigh") ? "high" : "low";
                    const target = Dice.get_target(message.chance, message.roll);
                    console.log("target:", target, "\n");
                    const ssh = Seed.get_server_hash_by_seed(seed_data.server_seed);
                    const ss = seed_data.server_seed;
                    const cs = seed_data.client_seed;
                    const payout = Dice.calculate_payout(message.chance);
                    const sn = 1;
                    const nb = nonce_data;
                    const result = Seed.get_result(ssh, ss, cs, sn, nb);
                    const won = (roll === "high") ? result > target : result < target;
                    const profit = (won) ? Dice.calculate_profit(message.chance, message.bet) : parseFloat(-1 * message.bet).toFixed(7);
                    const bet_details = [data.id, data.seed_detail_id, roll, won, message.bet, payout, profit, message.chance, target, result, nonce_data];

                    Bet.create(bet_details, function (bet_result_data) {
                        console.log("Created Bet");
                        const ret = {
                            bet_result_data,
                            user_balance: data.points + profit
                        };
                        callback(ret);
                    });
                });
            });
        }
    });
};

User.user_point_add = function (id, amount, callback) {
    db.query('UPDATE users SET points = points + ? where id = ?', [parseFloat(amount), id], function (err, rows) {
        if (err) {
            callback(err, null);
        } else {
            callback(null, rows);
        }
    });
};

User.transfer = function (from, to, amount, callback) {
    User.find(from, function (err, data) {
        if (err) {
            console.log(err);
            callback({ err: "Unknown User", code: 1 }, null);
        } else if (amount <= data.points) {
            User.user_point_add(from, -amount, function (err, from_data) {
                if (err) {
                    callback({ err: err, code: -1 }, null);
                } else {
                    User.user_point_add(to, amount, function (err, to_data) {
                        if (err) {
                            callback({ err: err, code: -1 }, null);
                        } else {
                            callback(null, { from: from_data, to: to_data, info: data });
                        }
                    });
                }
            });
        } else {
            callback({ err: "Insufficient Balance in:User:transfer", code: 2 }, null);
        }
    });
};

User.banker_point_add = function (amount, callback) {
    User.user_point_add(1, amount, callback);
};

User.find_by_name = function (name, callback) {
    db.query('SELECT * FROM users WHERE username = ?', [name], function (err, rows) {
        if (err) {
            callback(err, null);
        } else if (rows.length === 0) {
            callback(null, null);
        } else {
            callback(null, rows[0]);
        }
    });
};

User.is_present_by_name = function (name, callback) {
    User.find_by_name(name, function (err, result) {
        if (err) callback(err, null);
        else if (err == null && result == null) callback(null, false, null);
        else callback(null, true, result);
    });
};

User.set_name_by_gid = function (gid, name, callback) {
    db.query('UPDATE users SET username = ? WHERE gid = ?', [name, gid], function (err, rows) {
        console.log(err, rows);
        if (err) {
            console.log(err);
            callback(err, null);
        } else {
            callback(null, rows);
        }
    });
};

User.login = function (name, password, callback) {
    db.query("SELECT * FROM users WHERE username = ?", [name], function (err, rows) {
        if (err) {
            console.log(err);
            callback(0);
        } else {
            const pass = crypto.createHash('sha256').update(rows[0].gid + password).digest('hex');
            (pass === rows[0].password) ? callback(1) : callback(0);
        }
    });
};

User.setup_user_by = function (data, callback) {
    const pass = crypto.createHash('sha256').update(data.gid + data.password).digest('hex');
    db.query('UPDATE users SET username = ?, password = ? WHERE gid = ?', [data.username, pass, data.gid], function (err, rows) {
        if (err) {
            console.log(err);
            callback(err, null);
        } else {
            callback(null, rows);
        }
    });
};

User.create = function (gid, callback) {
    db.query('INSERT INTO users (points,gid) VALUES (100,?);', [gid], function (err, rows) {
        if (err) {
            console.log('Error creating user:', err); // Consider adding this for better error visibility
            callback(err, null);
        } else {
            callback(null, rows);
        }
    });
};

User.get_balance = function (id, callback) {
    db.query("SELECT points FROM users WHERE id= ?;", [id], function (err, rows) {
        if (err) {
            callback(err, null);
        } else {
            callback(err, rows[0].points);
        }
    });
};

User.page = function (pgno, callback) {
    db.query("SELECT id, username, points, gid FROM users;", function (err, rows) {
        callback(rows);
    });
};

export default User;

```

## C:\Users\tiach\Downloads\commands-for-dev\NodeJS\justdice\app\public\gambit.js
```
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
```

## C:\Users\tiach\Downloads\commands-for-dev\NodeJS\justdice\app\views\bet.ejs
```
<html>

<head>
    <title>Gambit: Bet Details</title>
    <link href="/bootstrap.min.css?body=1" media="all" rel="stylesheet" />
</head>

<body>
    <div class="container">
        <legend>Bet Details</legend>
        <table class="table table-bordered table-striped span6">
            <tbody>
                <tr>
                    <td>Bet Id</td>
                    <td>
                        <%= result.id %>
                    </td>
                </tr>
                <tr>
                    <td>Roll</td>
                    <td>
                        <%= result.roll %>
                    </td>
                </tr>
                <tr>
                    <td>Client Seed</td>
                    <td>
                        <%= seed.client_seed %>
                    </td>
                </tr>
                <tr>
                    <td>Server Seed</td>
                    <td>
                        <%= seed.server_hash %>
                    </td>
                </tr>
                <tr>
                    <td>Chance</td>
                    <td>
                        <%= parseFloat(result.chance).toFixed(7) %>
                    </td>
                </tr>
                <tr>
                    <td>Target</td>
                    <td>
                        <%= parseFloat(result.target).toFixed(7) %>
                    </td>
                </tr>
                <tr>
                    <td>Lucky</td>
                    <td>
                        <%= parseFloat(result.lucky).toFixed(7) %>
                    </td>
                </tr>
                <tr>
                    <td>Won</td>
                    <td>
                        <%= result.won %>
                    </td>
                </tr>
                <tr>
                    <td>Bet</td>
                    <td>
                        <%= parseFloat(result.bet).toFixed(7) %>
                    </td>
                </tr>
                <tr>
                    <td>Payout</td>
                    <td>
                        <%= parseFloat(result.payout).toFixed(7) %>
                    </td>
                </tr>
                <tr>
                    <td>Nonce</td>
                    <td>
                        <%= result.nonce %>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</body>

</html>
```

## C:\Users\tiach\Downloads\commands-for-dev\NodeJS\justdice\app\views\index.ejs
```
<!DOCTYPE html>
<html lang="en-US" style="color-scheme: light;">
<title>Gambit</title>

<head>

    <link href="/bootstrap-responsive.css?body=1" media="all" rel="stylesheet" />
    <link href="/bootstrap-responsive.min.css?body=1" media="all" rel="stylesheet" />
    <link href="/bootstrap-theme.css?body=1" media="all" rel="stylesheet" />
    <link href="/bootstrap-theme.min.css?body=1" media="all" rel="stylesheet" />
    <link href="/bootstrap.css?body=1" media="all" rel="stylesheet" />
    <link href="/bootstrap.min.css?body=1" media="all" rel="stylesheet" />
    <link href="/docs.css?body=1" media="all" rel="stylesheet" />
    <link href="/gambit.css" media="all" rel="stylesheet" />
    <script src="/jquery.min.js"></script>
    <script src="/bootstrap.min.js"></script>

    <script src="/socket.io/socket.io.js"></script>
</head>

<body>
    <div id="modal-login" class="modal">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
            <h4>Setup account</h4>
        </div>
        <div class="modal-body">
            <div class="row">
                <div class="col-sm-6 col-md-4 col-md-offset-4">
                    <div class="account-wall">
                        <img class="profile-img"
                            src="https://lh5.googleusercontent.com/-b0-k99FZlyE/AAAAAAAAAAI/AAAAAAAAAAA/eu7opA4byxI/photo.jpg?sz=120"
                            alt="">

                        <form class="form-signin" id="setup">
                            <div id="setup-alert">

                            </div>
                            <input type="text" class="form-control" placeholder="Username" id="username" required
                                autofocus>
                            <input type="password" class="form-control" placeholder="Password" id="password" required>
                            <button class="btn btn-lg btn-primary btn-block" type="submit">
                                Setup
                            </button>
                        </form>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <div id="modal" class="modal">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
            <h2>Invest or Divest</h2>
        </div>
        <div class="modal-body">
            <div class="row" id="invest-alert">

            </div>

            <h2>Invest</h2>

            <div class="box">
                <p>Lend some of your <span id="inv_balance" class="number-show">0.00000000</span> BTC balance to the
                    site
                    for
                    use as bankroll.</p>

                <p>You get any gains the site makes (minus a 10% commission on net profits), but you also take any
                    losses.</p>

                <div class="pad">
                    <div class="row">
                        <div class="span6">Increase investment? <input type="text" id="invest_input"> BTC</div>
                        <button class="btn" id="invest_few">invest</button>
                    </div>
                    <div class="row">
                        <div class="span6"> ... or invest your whole balance:
                            <button class="btn" id="invest_all">invest all</button>
                        </div>
                    </div>
                    <div class="clear"></div>
                    <div id="invest_error"></div>
                </div>
            </div>
            <br>

            <h2>Divest</h2>

            <div class="box">
                <div>Google tells me that 'divest' is the opposite of 'invest'. It's for getting your investment back
                    into
                    your
                    balance.
                </div>
                <div class="pad">
                    <div class="row">
                        <div class="span6">Reduce investment? <input id="divest_input"> BTC</div>
                        <button id="span3">divest</button>
                    </div>
                    <div class="row">
                        <div class="span6"> ... or divest your whole balance:
                            <button id="divest_all">divest all</button>
                        </div>
                    </div>
                    <div class="clear"></div>
                    <div id="divest_error"></div>
                </div>
            </div>
            <div class="row">
                <div class="span6">
                    <p>You currently have <span class="investment number-show">0.00000000</span> BTC
                        invested.</p>
                </div>
                <div class="span6">
                    <p>You are supplying <span class="invest_pct number-show">0.000000%</span> of the site's bankroll.
                    </p>
                </div>
            </div>
            <div class="clear"></div>

        </div>

    </div>
    <div id="modalr" class="modal">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
            <h2>Invest or Divest</h2>
        </div>
        <div class="modal-body">

            <div>
                <h2>Randomize Your Rolls</h2>

                <p>The last server seed was:</p>

                <div id="old_sseed" class="monospace number-show">
                    7pyGqC7VvOdipBaIAvVW52hHGk20RM6szsSGIx9_G6TskRWhnGzMK.0GIwFjbqOX
                </div>
                <p>The last server seed hash was:</p>

                <div id="old_shash" class="monospace number-show">
                    3163fa40fdd0827ede392b9e16648b1cbcf1c2f89a52e80cf4297cb83fe8c713
                </div>
                <p>Your client seed for that server seed was:</p>

                <div id="old_cseed" class="monospace number-show">164907815640242340165576</div>
                <p>The number of rolls you made with the last pair of seeds was:</p>

                <div id="old_nonce" class="monospace number-show">0</div>

                <div id="new_shash" class="monospace">9f20c0bd6b70eacad4cb3baeb450c656686841e179100c6b857f52bd8e26f19d
                </div>
                <p class="important">Type up to 24 random digits (0 through 9) to re-randomize with your own seed:</p>

                <div class="input_ok">
                    <div class="input_ok_input"><input id="new_cseed" class="seed_input" size="24" maxlength="24"
                            value="062843368122389680933683"></div>
                    <div class="fleft indent">
                        <button class="seed_button">ok</button>
                    </div>
                    <div class="clear"></div>
                </div>
                <div class="important" id="form_error"></div>
            </div>

        </div>

    </div>
    <div class="container">
        <legend>Welcome to Gambit</legend>
        <div class="panel panel-default">
            <div class="panel-heading">
                <h3 class="panel-title">Bet</h3>
            </div>
            <div class="panel-body">
                <div class="row">
                    <div class="span4">
                        <label class="span1">Chance:</label>

                        <div class="controls btn-group" style="margin: 0px">
                            <button class="btn btn-success setMinChance">min</button>
                            <button class="btn minus">-1</button>
                            <button class="btn plus">+1</button>
                            <button class="btn btn-danger setMaxChance">max</button>
                        </div>
                    </div>
                    <div class="span4">
                        <label class="span1">Bet:</label>

                        <div class="controls btn-group" style="margin: 0px">
                            <button class="btn btn-success setMinBet">min</button>
                            <button class="btn by2">/2</button>
                            <button class="btn mul2">*2</button>
                            <button class="btn btn-danger setMaxBet">max</button>
                        </div>
                    </div>
                    <!--</div>-->
                    <!--<div class="row">-->
                    <div class="span5">
                        <label class="span1">Action:</label>

                        <div class="controls btn-group" style="margin: 0px">
                            <button class="btn">Deposit</button>
                            <button class="btn">Widthdraw</button>
                            <button class="btn" data-toggle="modal" data-target="#modalr">Randomize</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="panel panel-primary">
            <div class="panel-heading">
                <h3 class="panel-title">Options</h3>
            </div>
            <div class="panel-body">
                <div class="row">
                    <div class="span3">
                        <div class="input-group input-group-sm">
                            <span class="input-group-addon">Chance to Win</span>
                            <input type="float" class="form-control right" id="chanceToWin" placeholder="">
                            <span class="input-group-addon">%</span>
                        </div>
                        <br>

                        <div class="input-group input-group-sm">
                            <span class="input-group-addon">Payout</span>
                            <input type="float" class="form-control right" id="payout" placeholder="">
                            <span class="input-group-addon">X</span>
                        </div>
                    </div>


                    <div class="span3">
                        <div class="input-group input-group-sm">
                            <span class="input-group-addon">Bet Size</span>
                            <input type="float" class="form-control right" id="betSize" placeholder="">
                            <span class="input-group-addon">Points</span>
                        </div>
                        <br>

                        <div class="input-group input-group-sm">
                            <span class="input-group-addon">Profit</span>
                            <input type="text" class="form-control right" id="profit" placeholder="">
                            <span class="input-group-addon">Points</span>
                        </div>
                    </div>
                    <div class="span3">
                        <button class="btn" id="high">Roll<br>Hi<br><span id="rhigh">
                                &lt; &nbsp; 12.00 </span></button>
                        <button class="btn" id="low">Roll<br>Low<br><span id="rlow">
                                &lt; &nbsp; 12.00 </span></button>
                    </div>
                    <div class="span2">
                        <span class="">Balance</span>
                        <span class="label label-primary" id="my_balance">0.0000000</span>

                    </div>
                </div>
                <div class="row" id="alert">

                </div>
            </div>
        </div>

        <div class="row">
            <div class="tabbable"> <!-- Only required for left/right tabs -->
                <ul class="nav nav-tabs">
                    <li class="active"><a href="#tab1" data-toggle="tab">Bets</a></li>
                    <li><a href="#tab4" data-toggle="tab">My Bets</a></li>
                    <li><a href="#tab2" data-toggle="tab">Invest</a></li>
                    <li><a href="#tab5" data-toggle="tab">Chat</a></li>
                    <li><a href="#tab6" data-toggle="tab">Account</a></li>
                    <li><a href="#tab3" data-toggle="tab">Fair?</a></li>
                </ul>
                <div class="tab-content">
                    <div class="tab-pane" id="tab5">
                        <div id="chat_view" class="panel hide">
                            <div id="" class="panel-heading">
                                <h3 class="panel-title">Enter Chat</h3>
                            </div>
                            <div class="panel-body">
                                <div id="actual_chat" class="panel">
                                    <div class="row">
                                        <div class="chatscroll">

                                        </div>
                                    </div>
                                    <div class="row">
                                        <div class="input-group input-group-sm span10">
                                            <span class="input-group-addon">Type the message</span>
                                            <input type="text" class="form-control"
                                                placeholder="enter your message here" id="chat_message">
                                            <span class="input-group-btn">
                                                <button class="btn btn-default" id="send_message"
                                                    type="button">Chat</button>
                                            </span>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="panel" id="chat_new">
                            <div class="row">
                                <div class="input-group input-group-sm span6">
                                    <span class="input-group-addon">Enter a name to start chatting</span>
                                    <input type="text" class="form-control" placeholder="Username" id="chat_username">
                                    <span class="input-group-btn">
                                        <button class="btn btn-default" id="start_chat" type="button">Chat</button>
                                    </span>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="tab-pane" id="tab6">

                        <p><b>Security Information</b></p>

                        <p>An account was automatically created when you first visited the site.
                            If you have cookies enabled, you will be automatically logged in each time you visit from
                            this computer.
                        </p>

                        <p>Your user ID is <span class="number-show userid"> 275810</span>.</p>

                        <p>You can log into the same account from a different computer or browser using this <a
                                id="log-link" href="/">link</a>.
                            Protect this secret link as it can be used to access your account balance.</p>

                        <p class="unset-account">If you prefer to use a more traditional and secure approach then
                            <button id="setup" class="btn btn-success" data-toggle="modal"
                                data-target="#modal-login">set up a username and
                                password.
                            </button>
                        </p>


                    </div>
                    <div class="tab-pane" id="tab4">
                        <p>All your bets come here</p>
                        <table class="table" id="myBets">
                            <thead>
                                <tr>
                                    <th>BetId</th>
                                    <th>Who</th>
                                    <th>When</th>
                                    <th>Lucky</th>
                                    <th>Target</th>
                                    <th>Bet</th>
                                    <th>Payout</th>
                                    <th>Profit</th>
                                </tr>
                            </thead>
                            <tbody>

                            </tbody>
                        </table>
                    </div>
                    <div class="tab-pane active" id="tab1">
                        <p>All bets come here</p>
                        <table class="table" id="incommingBets">
                            <thead>
                                <tr>
                                    <th>BetId</th>
                                    <th>Who</th>
                                    <th>When</th>
                                    <th>Lucky</th>
                                    <th>Target</th>
                                    <th>Bet</th>
                                    <th>Payout</th>
                                    <th>Profit</th>
                                </tr>
                            </thead>
                            <tbody>

                            </tbody>
                        </table>
                    </div>
                    <div class="tab-pane" id="tab2">
                        <div id="invest" style="display: block;">
                            <div class="panel">
                                <div clas="row">
                                    <div class="span5">
                                        <p>You currently have <span class="investment number-show">0.00000000</span> BTC
                                            invested.</p>
                                    </div>
                                    <div class="span1">
                                        <button id="invest_edit" class="btn" data-toggle="modal"
                                            data-target="#modal">edit</button>
                                    </div>
                                    <div class="span5 pull-right">
                                        <p>You are supplying <span class="invest_pct number-show">0.000000%</span> of
                                            the site's bankroll.
                                        </p>
                                    </div>
                                </div>
                                <div class="clear"></div>
                                <legend>Be the Bank!</legend>

                                <p>You can invest some of your balance with the site for other players to bet against.
                                    This both increases
                                    the maximum bets on the site, and you keep any profits made. You also 'keep' any
                                    losses.</p>

                                <p>Although we have a 1% house edge, and in the long run will earn a profit of 1% of the
                                    wagered amount, in
                                    the short to medium term we can still lose money. In times when we are lucky, we win
                                    many bets and earn
                                    a
                                    larger-than-expected profit, and in unlucky times we earn less than expected, and
                                    can even lose out.
                                    This
                                    is especially so if someone comes in and makes a large number of massive bets; we
                                    can either gain a lot
                                    or
                                    lose a lot.
                                    <b>If you believe that the potential gains do not outweigh the potential losses,
                                        please do not
                                        invest.</b>
                                </p>

                                <p>Let's break it down: Suppose the total bankroll is currently made of 90 BTC from a
                                    single investor, and
                                    you invest a further 10 BTC. You will have 10% of the new 'current bankroll', and
                                    the first investor's
                                    share will drop from 100% to 90%. Each bet that a player makes is played against the
                                    current bankroll.
                                    As
                                    players win and lose, your investment grows or shrinks by 10% of the overall house
                                    profit. When you
                                    withdraw your investment you get 10% of the current bankroll. You may withdraw your
                                    investment at any
                                    time. Other players' investments will affect the percentage of the current bankroll
                                    that your investment
                                    represents. If a 3rd investor then invests another 100 BTC, bringing the total
                                    bankroll to 200 BTC, the
                                    first investor's percentage drop from 90% to 45%, your percentage drops from 10% to
                                    5%, and the new
                                    investor's percentage is 50%. Then if a player loses 20 BTC to the site, everyone's
                                    investment grows in
                                    proportion. Your 10 BTC investment is now 5% of the new bankroll (220 BTC) ie. 11
                                    BTC.</p>

                                <p>On each bet, each player can profit by up to 0.5% of the house's bankroll. The
                                    maximum bet is dynamically
                                    adjusted after each bet. Work is in progress to allow investors to set their own
                                    risk level. Perhaps you
                                    want to risk up to 5% of your investment on each roll, not just 1%. At some point
                                    that may be available.
                                    Originally the site allowed players to profit by up to 1% of the house's bankroll,
                                    but this figure was
                                    reduced in an attempt to reduce volatility in the bankroll levels.</p>

                                <p>A simple example: The site's bankroll is 90 BTC. You invest 10 BTC, bringing the
                                    total bankroll up to 100
                                    BTC. A player bets 1 BTC and loses. The total bankroll is now 101 BTC. You withdraw
                                    your investment, and
                                    get 10.1 BTC. The site's bankroll is now 90.9 BTC.</p>

                                <p>Alternatively: You invest the same 10 BTC and the same player bets 1 BTC at a 2x
                                    multiplier and wins. The
                                    total bankroll is now 99 BTC. Your investment is now only worth 9.9 BTC. You can
                                    withdraw it now and
                                    take
                                    the loss, or wait for the law of large numbers to work in your favour. In the long
                                    run you can expect to
                                    profit 1% of everything bet against your investment.</p>

                                <p>The site currently charges a 10% commission on net investment profits to cover
                                    expenses such as
                                    advertising, server hosting, etc. The commission rate is subject to change. Notice
                                    will be given in this
                                    paragraph 7 clear days before any rate change takes effect.</p>

                                <p>Commission is charged when profits are divested, or at midnight (UTC) on Sunday each
                                    week, whichever
                                    happens sooner. Commission is never charged twice on the same profits. For example
                                    if you invest 100 BTC
                                    and it grows to 110 BTC by the end of the first week, you will be charged 10% of
                                    your 10 BTC profit. If
                                    your remaining 109 BTC investment then shrinks to 105 BTC over the next week, you
                                    will not be charged
                                    any
                                    commission at the end of that week. And then, if it grows to 119 BTC by the end of
                                    the 3rd week, you
                                    will
                                    only be charged 10% commission on the new 10 BTC of profit over the previous high of
                                    109 BTC. At any
                                    point
                                    you could divest up to your original investment of 100 BTC without being charged
                                    commission since we
                                    consider that when divesting you divest the original investment first, and profits
                                    later.</p>

                                <p>Please help advertise the site. The more players we have, the faster your investment
                                    will grow. If you
                                    have a BitcoinTalk.org forum account, please consider adding the following to your
                                    signature there:</p>

                                <div class="code">
                                    [size=14pt][font=Arial][b][glow=#6a6,2,300][url=https://just-dice.com][color=#fff]&nbsp;♦&nbsp;&nbsp;Just-Dice.com&nbsp;&nbsp;♦&nbsp;[/color][/url][/glow]&nbsp;&nbsp;[glow=#6a6,2,300][url=https://just-dice.com][color=#fff]&nbsp;♦&nbsp;&nbsp;1%
                                    House Edge Dice
                                    Game&nbsp;&nbsp;♦&nbsp;[/color][/url][/glow]&nbsp;&nbsp;[glow=#6a6,2,300][url=https://just-dice.com][color=#fff]&nbsp;♦&nbsp;&nbsp;Play
                                    or Invest&nbsp;&nbsp;♦&nbsp;[/color][/url][/glow][/b][/font][/size]
                                </div>
                                <p>To edit your BitcoinTalk signature, visit
                                    <a href="https://bitcointalk.org/index.php?action=profile"
                                        target="_blank">https://bitcointalk.org/index.php?action=profile</a>
                                    then click the "Forum Profile Information" link under "Modify Profile" in the top
                                    left. Copy/paste the
                                    above code into the "Signature" box, and click "Change profile" at the bottom of the
                                    page to save the
                                    new
                                    signature.
                                </p>
                            </div>
                        </div>
                    </div>
                    <div class="tab-pane" id="tab3">
                        <div class="panel">
                            <h3>Provable Fairness Overview</h3>

                            <p>This game is provably fair. What that means is that there is no way the site can cheat
                                you by picking
                                numbers to make you lose. You can take our word for it, but for the crypto-nerds out
                                there, here are the
                                gory details:</p>

                            <p>When you click 'randomize' in the top right we make up a secret random string (the server
                                seed) that is
                                used to randomize the rolls. You are shown the hash of the server seed, and are asked to
                                supply your own
                                random number (the client seed) to further randomize the rolls.</p>

                            <p>The sha256 hash of the server seed you are currently using is:</p>

                            <div class="monospace">
                                <span id="shash" class='number-show'></span>
                            </div>
                            <p></p>

                            <p>The client seed currently in use:</p>

                            <div class="monospace"><span id="seed" class="number-show"></span></div>
                            <p></p>

                            <p>and the number of bets you have made using it:</p>

                            <div class="monospace"><span id="nonce" class="number-show">0</span></div>
                            <p></p>

                            <p>Each time you roll, the server and client seeds are combined with the number of rolls you
                                have made since
                                the seeds were selected to create the roll.</p>

                            <p>Notice that you are shown the hash of the server seed <em>before</em> picking your client
                                seed. This
                                ensures that there is no way we can influence the numbers you will roll.</p>

                            <h3>Instant Verification with a Single Seed</h3>

                            <p>If you want to verify that we are not cheating you, click 'randomize' again to reveal the
                                current server
                                seed and generate a new pair of seeds for future rolls.</p>

                            <p>In this way you can verify your rolls whenever you like, without having to wait for a
                                daily secret to be
                                published, and you are safe from cheating without the need to set a different client
                                seed for each bet you
                                make.</p>

                            <h3>Details</h3>
                            <h4>For bets :</h4>

                            <p>To generate your dice rolls, we string together your bet number, a colon, your client
                                seed, a colon, and
                                your bet number.</p>

                            <p>For example, if your client seed is 1234567 and you are about to make your first roll
                                since setting the
                                seed, we will use "1:1234567:1".</p>

                            <p>We do the same with the server seed: put your bet number before and after it, with a
                                colon separator.</p>

                            <p>We then use the hmac-sha512() function to hash that string with the modified server seed.
                                That gives us a
                                128 character hex string.</p>
                            <h4>For all bets:</h4>

                            <p>Note that the "bet number" in both the above cases is the number of bets you have made
                                since your seeds
                                were selected, not the global server "bet ID" number.</p>

                            <p>We then take the first 5 characters of that hex string and convert them to a decimal
                                integer (that will
                                be in the range 0 through 1048575 (16^5-1)).</p>

                            <p>If it is less than 1 million, we divide it by 10,000 and use it as your dice roll. That
                                is the case 96%
                                of the time.</p>

                            <p>Otherwise we use the next five characters of the 128 character hex string, and repeat.
                            </p>

                            <p>In the unlikely event that none of the 25 groups of five characters are lower than 1
                                million when
                                convered to decimal, we use the remaining 3 hex digits, which give a number in the range
                                0 through 4095,
                                which corresponds to a dice roll of 0.0000 through 0.4095.</p>

                            <h3>Verifier</h3>

                            <p>A few players on the site collaborated to create
                                <a target="_blank" href="http://bitcoinmaniac.com/justdice">a service which you can
                                    use</a> to verify your
                                rolled numbers. Copy the 3-line value from the 'randomize' window into the first input
                                of that page and
                                click 'verify' for a list of the numbers you rolled, calculated independently of the
                                site.
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <script>

        var house_edge = 1;
        var user_name = "";

        function recalculate(id) {
            var value = parseFloat($('#' + id).val()).toFixed(7);
            switch (id) {
                case "chanceToWin":
                    $('#payout').val(((100 - house_edge) / value).toFixed(7));
                    $('#profit').val(((parseFloat($('#payout').val()).toFixed(7) - 1) * $('#betSize').val()).toFixed(7));
                    $('#rlow').text("<" + String(parseFloat($('#' + id).val()).toFixed(7)));
                    $('#rhigh').text(">" + String((99.99999 - parseFloat($('#' + id).val())).toFixed(7)));

                    break;
                case "payout":
                    $('#chanceToWin').val(((100 - house_edge) / value).toFixed(7));
                    $('#profit').val((($('#payout').val() - 1) * $('#betSize').val()).toFixed(7));
                    $('#rlow').text("<" + String(parseFloat($('#chanceToWin').val()).toFixed(7)));
                    $('#rhigh').text(">" + String((99.99999 - parseFloat($('#chanceToWin').val())).toFixed(7)));
                    break;
                case "betSize":
                    $('#profit').val((($('#payout').val() - 1) * value).toFixed(7));
                    break;
                case "profit":
                    $('#betSize').val((value / ($('#payout').val() - 1)).toFixed(7));
                    break;
            }
        }

        $('#chanceToWin,#betSize,#payout,#profit').bind('input', function (e) {
            var charCode = e.keyCode;

            if ((charCode > 31 && charCode != 46 && charCode != 8 && (charCode < 48 || charCode > 57))) {
                return false;
            }
            if ($(this).attr("id") == "chanceToWin") {
                if ($(this).val() > 100) {
                    $(this).val(100);
                }
            }
            recalculate($(this).attr("id"), this.value);
            return true;
        })

        $('#chanceToWin,#betSize,#payout,#profit').bind('input', function (e) {

        })


        $('.plus').mousedown(function () {
            $('#chanceToWin').val(parseFloat($('#chanceToWin').val()) + 1);
            recalculate('chanceToWin');
        });

        $('.minus').mousedown(function () {
            $('#chanceToWin').val(parseFloat($('#chanceToWin').val()) - 1);
            recalculate('chanceToWin');
        });

        $('.setMaxChance').mousedown(function () {
            $('#chanceToWin').val(parseFloat(95));
            recalculate('chanceToWin');
        });

        $('.setMinChance').mousedown(function () {
            $('#chanceToWin').val(parseFloat(1));
            recalculate('chanceToWin');
        });

        $('.by2').mousedown(function () {
            $('#betSize').val(parseFloat($('#betSize').val()) / 2);
            recalculate('betSize');
        });

        $('.mul2').mousedown(function () {
            $('#betSize').val(parseFloat($('#betSize').val()) * 2);
            recalculate('betSize');
        });

        $('.setMaxBet').mousedown(function () {
            $('#betSize').val(parseFloat($("#my_balance").text()).toFixed(7));
            recalculate('betSize');
        });

        $('.setMinBet').mousedown(function () {
            $('#betSize').val(parseFloat(0.01));
            recalculate('betSize');
        });


        $('#chanceToWin').val(49.5);
        $('#betSize').val("1");
        recalculate("chanceToWin");
        recalculate("betSize");

    </script>

    <script>
        var current_user = "";
        var bet_id_data = {};
        var socket;
        var set_bal;
        var setup_done = 0;

        function getCookie(c_name) {
            var c_value = document.cookie;
            var c_start = c_value.indexOf(" " + c_name + "=");
            if (c_start == -1) {
                c_start = c_value.indexOf(c_name + "=");
            }
            if (c_start == -1) {
                c_value = null;
            }
            else {
                c_start = c_value.indexOf("=", c_start) + 1;
                var c_end = c_value.indexOf(";", c_start);
                if (c_end == -1) {
                    c_end = c_value.length;
                }
                c_value = unescape(c_value.substring(c_start, c_end));
            }
            return c_value;
        }

        $(document).ready(function () {
            // IO
            socket = io.connect(document.location.protocol + '//' + document.location.hostname + ":3000");

            console.log(`Cookies: ${document.cookie}`);
            const _gid = fetch('/api/gid')
                .then(response => response.json())
                .then(data => {
                    const gid = data.gid;
                    // Sử dụng gid tại đây
                    console.log(`gid: ${gid}`);
                    return gid;
                });

            $('#start_chat').click(function (event) {
                socket.emit("message", { action: "username", gid: getCookie("gambit_guid"), name: $('#chat_username').val() });
            });

            $('#send_message').click(function (event) {
                socket.emit("chat", { gid: getCookie("gambit_guid"), name: $('#username').val(), message: $('#chat_message').val() });
                $('#chat_message').val("");
            });

            $("#chat_message").keyup(function (event) {
                if (event.keyCode == 13) {
                    $("#send_message").click();
                }
            });

            set_bal = function (val) {
                $('#my_balance').html(parseFloat(val).toFixed(7));
                $('#inv_balance').html(parseFloat(val).toFixed(7));
            }

            // Ready
            function my_bet(bet, is_my_bet) {
                var str = '<tr class="' + (bet.won ? 'success' : 'danger') + '">'
                    + '<td><a href="/bet/' + bet.id + '" target="_blank" >BET' + bet.id + '</a></td>'
                    + '<td>' + bet.user_id + '</td>'
                    + '<td>' + bet.created_at + '</td>'
                    + '<td>' + bet.lucky + '</td>'
                    + '<td>' + ((bet.roll == "high") ? '> ' : '&lt; &nbsp;') + bet.target + '</td>'
                    + '<td>' + bet.bet + '</td>'
                    + '<td>' + bet.payout + '</td>'
                    + '<td>' + bet.profit + '</td>'
                    + '</tr>';
                console.log(str);
                if (is_my_bet)
                    $("#myBets tbody").prepend(str);
                else
                    $("#incommingBets tbody").prepend(str);

            }

            var alert = $('#alert');
            $(function () {
                socket.on('message', function (message) {
                    switch (message.action) {
                        case 'seed_data':
                            alert.html('');
                            $('#shash').text(message.ssh);
                            $('#seed').text(message.cs);
                            $('#nonce').text(message.nonce);
                            $('.userid').html(message.id);
                            $('#log-link').attr('href', document.location.protocol + '//' + document.location.hostname + ":3000/login/" + message.gid);
                            if (message.setup) {
                                $('.unset-account').hide();
                                setup_done = 1;
                            }
                            set_bal(message.balance);

                            if (message.name) {
                                user_name = message.name;
                                $('#chat_view').removeClass("hide");
                                $('#chat_new').addClass("hide");
                            }
                            break;
                        case 'new_bet':
                            my_bet(message, 0);
                            break;
                        case 'old_bet':
                            $.each(message.bets, function (key, bet) {
                                my_bet(bet, 0);
                            })
                            break;
                        case 'my_old_bet':
                            $.each(message.bets, function (key, bet) {
                                my_bet(bet, 1);
                            })
                            break;
                        case 'new_name':
                            alert.html('');
                            user_name = message.name;
                            $('#chat_view').removeClass("hide");
                            $('#chat_new').addClass("hide");
                            break;

                        case 'my_bet':
                            my_bet(message, 1);
                            break;
                        case "insuf_balance":
                            alert.html('');
                            alert.append('<div class="alert alert-danger bs-alert-old-docs span3">' + 'Insufficient balance' + '</div>');
                            break;
                    }
                    console.log('received message:', message);
                });

                socket.on('connect', function (message) {
                    socket.emit('justnow', { gid: getCookie("gambit_guid") });
                });

                socket.on('balance', function (message) {
                    set_bal(message);
                });

                socket.on('chat', function (message) {
                    var chat = $('.chatscroll');
                    chat.append("<div class='chatline'><b>#" + message.from + ":->&nbsp&nbsp</b>" + message.message + "</div>");
                    chat.scrollTop(chat.scrollTop() + 100);
                });

                socket.on('error', function (error) {
                    console.log(error);
                    if (!error) return;
                    var alert = $('#' + error.display);
                    alert.html('');
                    alert.append('<div class="alert alert-danger bs-alert-old-docs span6">' + error.message + '</div>');
                    alert.show().delay(5000).fadeOut();
                });

                // Send Message
                $('#high,#low').click(function (event) {
                    var alert = $('#alert');
                    if (parseFloat($('#my_balance').html()) < parseFloat($('#betSize').val())) {
                        alert.html('');
                        alert.append('<div class="alert alert-danger bs-alert-old-docs span12">' + 'Insufficient balance' + '</div>');
                        return;
                    } else {
                        alert.html('');
                    }
                    var message = {
                        action: "new-bet",
                        chance: $('#chanceToWin').val(),
                        bet: $('#betSize').val(),
                        roll: 'r' + $(this).attr("id"),
                        gid: getCookie("gambit_guid")
                    };
                    console.log('send message:', message);
                    socket.emit('message', message);
                });

                socket.on('disconnect', function () {
                    console.log('disconnect')
                });
            });
        })
    </script>
    <script src="gambit.js"></script>
</body>

</html>
```

## C:\Users\tiach\Downloads\commands-for-dev\NodeJS\justdice\app\views\users.ejs
```
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gambit: User Details</title>
    <link href="//netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css" rel="stylesheet">
    <script src="http://code.jquery.com/jquery-2.0.3.min.js"></script>
    <script src="//netdna.bootstrapcdn.com/bootstrap/3.0.0/js/bootstrap.min.js"></script>
    <link href="//cdnjs.cloudflare.com/ajax/libs/x-editable/1.5.0/bootstrap3-editable/css/bootstrap-editable.css"
        rel="stylesheet" />
    <script
        src="//cdnjs.cloudflare.com/ajax/libs/x-editable/1.5.0/bootstrap3-editable/js/bootstrap-editable.min.js"></script>
</head>

<body>
    <div class="container">
        <legend>User Details</legend>
        <table class="table table-striped">
            <thead>
                <tr>
                    <th style='width:10px'>S.No</th>
                    <th style='width:10px'>ID</th>
                    <th>Name</th>
                    <th>Points</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                <% users.forEach((user, index)=> { %>
                    <tr>
                        <td>
                            <%= index + 1 %>
                        </td>
                        <td>
                            <%= user.id %>
                        </td>
                        <td>
                            <% if(user.username) { %>
                                <%= user.username %>
                                    <% } else { %>
                                        <span style='color:#aaaaaa'>NULL</span>
                                        <% } %>
                        </td>
                        <td>
                            <a href="#" id="points" data-type="text" data-pk="<%= user.id %>" data-title="Enter points"
                                class="editable editable-click points">
                                <%= user.points %>
                            </a>
                        </td>
                        <td>edit</td>
                    </tr>
                    <% }); %>
            </tbody>
        </table>
    </div>

    <script>
        function getCookieValue(key) {
            var cookies = document.cookie.split('; ');
            for (var i = 0, parts; (parts = cookies[i] && cookies[i].split('=')); i++) {
                if (decode(parts.shift()) === key) {
                    return decode(parts.join('='));
                }
            }
            return null;
        }

        function decode(s) {
            return decodeURIComponent(s.replace(/\+/g, ' '));
        }

        $.fn.editable.defaults.mode = 'popup';
        $(document).ready(function () {
            $('.points').editable({
                type: 'text',
                url: '/admin/user/edit',
                title: 'Enter new points',
                success: function (response, newValue) {
                    // Xử lý sau khi cập nhật thành công (nếu cần)
                    console.log('Points updated!');
                }
            });
        });
    </script>
</body>

</html>
```

