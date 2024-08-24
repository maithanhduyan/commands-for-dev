import crypto from 'crypto';
import Seed from './seed.js';
import User from './users.js';

export function checkAndSetCookie(req, res, next) {
    const appCookieName = 'gambit_guid';
    
    if (!req.cookies[appCookieName]) {
        // Tạo cookie mới với giá trị UUID hoặc giá trị độc nhất khác
        let gid = crypto.createHash('md5').update(Seed.create_client_seed()).digest('hex');
        let points = 0;
        res.cookie(appCookieName, gid, { maxAge: 900000, httpOnly: false, sameStie:'None' });
        User.create(gid, function (err, success){
            console.log(`Tạo gid: ${gid} mới và points: ${points}`)
        })
        console.log(`Cookie mới được tạo: ${gid}`);
    } else {
        console.log(`Cookie đã tồn tại: ${req.cookies[appCookieName]}`);
    }
    next(); // Chuyển tiếp sang middleware hoặc route tiếp theo
}