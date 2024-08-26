
import mysql2 from 'mysql2';
import dotenv from 'dotenv';

dotenv.config();

// Truy cập biến môi trường
const dbHost = process.env.DB_HOST;
const dbName = process.env.DB_NAME;
const dbPort = process.env.DB_PORT;
const dbUser = process.env.DB_USER;
const dbPass = process.env.DB_PASSWORD;

export const connection = mysql2.createConnection({
    host: dbHost,
    database: dbName,
    user: dbUser,
    password: dbPass,
});

connection.connect(function (err) {
    if (err) throw err;
    console.log('Connected to the database!');
});

export default connection;


