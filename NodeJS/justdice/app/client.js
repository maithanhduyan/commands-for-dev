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
