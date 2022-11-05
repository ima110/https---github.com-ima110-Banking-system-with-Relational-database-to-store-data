CREATE DATABASE Banking
    DEFAULT CHARACTER SET = 'utf8mb4';
USE Banking;

CREATE TABLE user_info(name CHAR(100) NOT NULL,age INT NOT NULL,gender CHAR(50),National_id BIGINT NOT NULL, PRIMARY KEY(National_id));

SHOW COLUMNS in user_info;

CREATE Table Account_info(Account_no BIGINT NOT NULL,Balance DECIMAL DEFAULT 0.00, PRIMARY KEY(Account_no));

SHOW columns in Account_info;

CREATE TABLE login_info(E_mail_id VARCHAR(100) NOT NULL,password VARCHAR(100) NOT NULL, PRIMARY KEY(E_mail_id));

SHOW columns in login_info;

CREATE Table user_details(user_id VARCHAR(100) NOT NULL,Account_no BIGINT NOT NULL,National_id BIGINT NOT NULL,
                          E_mail_id VARCHAR(100) NOT NULL, PRIMARY KEY(user_id),FOREIGN KEY(Account_no) REFERENCES
                           Account_info(Account_no), FOREIGN KEY(National_id) REFERENCES user_info(National_id),
                           FOREIGN KEY(E_mail_id) REFERENCES login_info(E_mail_id));


SHOW columns IN user_details;