# Directory tree of C:\Users\tiach\Downloads\commands-for-dev\NodeJS\justdice\app

├── app/
│   ├── admin.js
│   ├── analytic.py
│   ├── app.js
│   ├── bet.js
│   ├── cache.js
│   ├── chat.js
│   ├── client.js
│   ├── connect.js
│   ├── dice.js
│   ├── error_code.js
│   ├── invest.js
│   ├── justdice.sql
│   ├── package-lock.json
│   ├── package.json
│   ├── redis.js
│   ├── seed.js
│   ├── seed_detail.js
│   └── users.js
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

```

## C:\Users\tiach\Downloads\commands-for-dev\NodeJS\justdice\app\app.js
```
import express from 'express';
import http from 'http';
import Seed from './seed.js';
import Bet from './bet.js';
import dice from './dice.js';
import User from './users.js';
import SeedDetail from './seed_detail.js';
import err_code from "./error_code.js";
import Chat from "./chat.js";
import Pool from "./client.js";
import Invest from "./invest.js";
import path from "path";
import crypto from 'crypto';
import Admin from './admin.js';
import { Server as SocketIOServer } from 'socket.io';
import { createServer } from 'http';
import connectDB from './connect.js'; // Import module kết nối MySQL
import cookieParser from 'cookie-parser';
import morgan from 'morgan';
import methodOverride from 'method-override'; // Import method-override

var ipaddr = process.env.OPENSHIFT_NODEJS_IP || "127.0.0.1";
var port = process.env.OPENSHIFT_NODEJS_PORT || 1337;

const app = express();
const httpServer = createServer(app);
const io = new SocketIOServer(httpServer);

// Thiết lập cổng cho ứng dụng
app.set('port', process.env.PORT || port);

// Thiết lập các middleware
app.use(morgan('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(cookieParser()); // Sử dụng cookie-parser để phân tích cookies
app.use(methodOverride('_method')); // Sử dụng methodOverride để hỗ trợ PUT/DELETE trong form HTML

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

// Kết nối MySQL
let db;
const connectDatabase = async () => {
    db = await connectDB();
};

connectDatabase().catch(err => console.error('Failed to connect to MySQL:', err));

// Route 
app.get('/users', async (req, res) => {
    const [rows] = await db.execute('SELECT * FROM users');
    res.render('index', { users: rows });
});

app.get("/", async (req, res) => {
    console.log("\n\n\n\n\nCookies");
    console.log(req.cookies);
    if (!(req.cookies.gambit_guid)) {
        var gid = crypto.createHash('md5').update(Seed.create_client_seed()).digest('hex');
        res.cookie('gambit_guid', gid);
        User.create(gid, function (err, success) {
            res.redirect("/index.html");
        });
    } else
        res.redirect("/index.html");
});

// Socket.IO 
// io.on('connection', (socket) => {
//     console.log('A user connected');
//     socket.on('message', (msg) => {
//         console.log('Message received:', msg);
//     });

//     socket.on('disconnect', () => {
//         console.log('User disconnected');
//     });
// });

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
        if (!message.gid) {
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
    console.log(`Server running at http://${ipaddr}:${app.get('port')}/`);
});
```

## C:\Users\tiach\Downloads\commands-for-dev\NodeJS\justdice\app\bet.js
```
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

import mysql from 'mysql2/promise';

const connectDB = async () => {
  try {
    const connection = await mysql.createConnection({
      host: 'localhost',
      user: 'admin',
      password: 'admin@2024', // Thay thế bằng mật khẩu MySQL của bạn
      database: 'justdice'
    });

    console.log('Connected to MySQL Database');
    return connection;
  } catch (error) {
    console.error('Error connecting to MySQL Database:', error);
    throw error;
  }
};

export default connectDB;

```

## C:\Users\tiach\Downloads\commands-for-dev\NodeJS\justdice\app\dice.js
```
const Dice = {};

Dice.get_target = function (chance, roll) {
    chance = parseFloat(chance).toFixed(7);
    if (roll === "rhigh")
        return (99.999999 - chance).toFixed(7);
    return chance.toFixed(7);
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
                    console.log("target:", target, "\n\n\n\n\n\n");
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
            const pass = crypto.createHash('md5').update(rows[0].gid + password).digest('hex');
            (pass === rows[0].password) ? callback(1) : callback(0);
        }
    });
};

User.setup_user_by = function (data, callback) {
    const pass = crypto.createHash('md5').update(data.gid + data.password).digest('hex');
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
        callback(err, rows);
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
    db.query("SELECT * FROM users;", function (err, rows) {
        callback(rows);
    });
};

export default User;

```

## C:\Users\tiach\Downloads\commands-for-dev\NodeJS\justdice\app\public\gambit.js
```
/**
 * Created with JetBrains WebStorm.
 * User: hariharasudhan
 * Date: 21/11/13
 * Time: 7:13 AM
 * To change this template use File | Settings | File Templates.
 */
$(function () {
    $('#randomize').click(function (event) {

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
                        <%= result.chance.toFixed(7) %>
                    </td>
                </tr>
                <tr>
                    <td>Target</td>
                    <td>
                        <%= result.target.toFixed(7) %>
                    </td>
                </tr>
                <tr>
                    <td>Lucky</td>
                    <td>
                        <%= result.lucky.toFixed(7) %>
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
                        <%= result.bet.toFixed(7) %>
                    </td>
                </tr>
                <tr>
                    <td>Payout</td>
                    <td>
                        <%= result.payout.toFixed(7) %>
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
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Node.js Project</title>
</head>

<body>
    <h1>User List</h1>
    <ul>
        <% users.forEach(user=> { %>
            <li>
                <%= user.name %>
            </li>
            <% }) %>
    </ul>

    <script src="/socket.io/socket.io.js"></script>
    <script>
        const socket = io();
        socket.emit('message', 'Hello from client!');
    </script>
</body>

</html>
```

## C:\Users\tiach\Downloads\commands-for-dev\NodeJS\justdice\app\views\users.ejs
```
<html>

<head>
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
                    <td style='width:10px'>S.No</td>
                    <td style='width:10px'>Id</td>
                    <td>Name</td>
                    <td>points</td>
                    <d>
                        <td>
                <tr>
            </thead>
            <tbody>
                <% for (i=0;i<data.length;i++){ %>
                    <tr>
                        <td>
                            <%= i %>
                        </td>
                        <td>
                            <%= data[i].id %>
                        </td>
                        <td>
                            <% if(data[i].username) {%>
                                <%= data[i].username %>
                                    <% }else { %>
                                        <span style='color:#aaaaaa'>NULL</span>
                                        <% } %>
                        </td>
                        <td><a href="#" id="points" data-type="text" data-pk="<%= data[i].id %>"
                                data-title="Enter username" class="editable editable-click points">
                                <%= data[i].points %>
                            </a></td>
                        <td>edit</td>
                    <tr>
                        <% } %>
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
                pk: 1,
                url: '/admin/user/edit',
                title: 'Enter username',
            });
        });
    </script>
</body>

</html>
```

