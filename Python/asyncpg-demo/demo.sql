-- Tạo database
CREATE DATABASE asyncpgdb;

-- Kết nối tới database
\c asyncpgdb;

-- Tạo bảng demo
CREATE TABLE demo (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

-- Thêm dữ liệu mẫu vào bảng demo
INSERT INTO demo (name) VALUES ('Alice');
INSERT INTO demo (name) VALUES ('Bob');
INSERT INTO demo (name) VALUES ('Charlie');
INSERT INTO demo (name) VALUES ('David');
INSERT INTO demo (name) VALUES ('Eve');