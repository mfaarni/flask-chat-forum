
CREATE TABLE users 
(id SERIAL PRIMARY KEY,
username TEXT UNIQUE, 
password TEXT, 
role INTEGER);


CREATE TABLE topics 
(id SERIAL PRIMARY KEY,
topic TEXT UNIQUE);

CREATE TABLE posts 
(id SERIAL PRIMARY KEY, 
title  TEXT, 
content TEXT, 
user_id INTEGER, 
visibility BOOLEAN,
created TIMESTAMP,
topic_id INTEGER);

CREATE TABLE comments 
(id SERIAL PRIMARY KEY, 
content  TEXT, 
user_id INTEGER, 
post_id INTEGER,
visibility BOOLEAN,
created TIMESTAMP);

CREATE TABLE quotes
(id SERIAL PRIMARY KEY,
content TEXT,
user_id INTEGER);



