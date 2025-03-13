--@block
CREATE TABLE Users(
  id INT PRIMARY KEY AUTO_INCREMENT,
  email VARCHAR(255) NOT NUll UNIQUE,
  bio TEXT,
  country VARCHAR(2)
);

--@block
INSERT INTO Users (email, bio, country)
VALUES (
  'hello@gmail.com',
  'I like traveling',
  'US'
);

--@block
CREATE TABLE Messages (
  id INT PRIMARY KEY AUTO_INCREMENT,
  message VARCHAR(120) NOT NUll UNIQUE
);

--@block
INSERT INTO Messages (message)
VALUES (
  'hello first message'
);

--@block
SELECT * FROM Messages

--@block
DROP TABLE Messages;

--@block
INSERT INTO core_messages(message)
VALUES(
  'hello First Message'
);

--@block
SELECT * FROM core_messages

--@block
SELECT * FROM auth_user

--@block
DELETE FROM `core_messages` WHERE `id` IN (1,3);

--@block
ALTER TABLE core_messages AUTO_INCREMENT = 1

--@block
SELECT * FROM users

--@block 
SELECT * FROM auth_user

--@block 
SELECT * FROM core_user

--@block
SELECT * FROM core_account