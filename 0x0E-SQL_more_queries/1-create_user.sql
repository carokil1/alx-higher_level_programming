-- creates the MySQL server user usd_1 and grants permission
SELECT user FROM mysql.user WHERE user = 'user_0d_1';
CREATE USER IF NOT EXISTS user_0d_1@localhost IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO user_0d_1@localhost WITH GRANT OPTION;
FLUSH PRIVILEGES;
