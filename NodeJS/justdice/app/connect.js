
// import mysql from 'mysql2/promise';

// const connectDB = async () => {
//   try {
//     const connection = await mysql.createConnection({
//       host: 'localhost',
//       user: 'admin',
//       password: 'admin@2024', // Thay thế bằng mật khẩu MySQL của bạn
//       database: 'justdice'
//     });

//     console.log('Connected to MySQL Database');
//     return connection;
//   } catch (error) {
//     console.error('Error connecting to MySQL Database:', error);
//     throw error;
//   }
// };
// 

import mysql from 'mysql2';

const connection = mysql.createConnection({
    host: 'localhost',
    user: 'admin',
    password: 'admin@2024',
    database: 'justdice'
});

connection.connect(function(err) {
    if (err) throw err;
    console.log('Connected to the database!');
});

export default connection;


