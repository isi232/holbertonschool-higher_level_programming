-- creates user_0d_1 password should be set to user_0d_1_pwd
-- grants the user all privileges on the entire MySQL server.
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
