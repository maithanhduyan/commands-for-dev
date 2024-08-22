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
