-- creating a user and granting privileges
CREATE USER IF NOT EXISTS user_0d_1@localhost IDENTIFIED BY user_0d_1_pwd;
GRANT ALL PRIVILEGES *.* TO user_0d_1@localhost;