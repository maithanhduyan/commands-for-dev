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