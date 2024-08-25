
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