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
