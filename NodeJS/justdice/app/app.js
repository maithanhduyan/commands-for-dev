import express from 'express';
import Seed from './seed.js';
import Bet from './bet.js';
import User from './users.js';
import SeedDetail from './seed_detail.js';
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
import { checkAndSetCookie } from './middleware.js';

dotenv.config();

var ipaddr = process.env.OPENSHIFT_NODEJS_IP || "127.0.0.1";
var port = process.env.SERVER_PORT || 3000;

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
app.use(checkAndSetCookie);
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

// Initialize Admin
Admin.initialize(app);

// API Route
app.get('/api/gid', (req, res) => {
    const gid = req.cookies.gambit_guid;
    res.json({ gid: gid });
});

// Route 
app.get("/", function (req, res) {
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