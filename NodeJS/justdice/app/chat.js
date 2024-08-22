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
