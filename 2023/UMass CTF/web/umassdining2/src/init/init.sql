CREATE DATABASE IF NOT EXISTS umassdining;
USE umassdining;

CREATE TABLE users 
(username VARCHAR(255), password VARCHAR(255));

INSERT INTO users (username,password) 
VALUES 
('admin','testin');