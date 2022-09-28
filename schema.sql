CREATE TABLE posts 
(id SERIAL PRIMARY KEY, 
title  TEXT, 
content TEXT, 
user_id INTEGER, 
created TIMESTAMP);


CREATE TABLE users 
(id SERIAL PRIMARY KEY,
username TEXT UNIQUE, 
password TEXT, 
role INTEGER);
