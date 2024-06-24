CREATE TABLE student(
	student_id SERIAL PRIMARY KEY,
	name VARCHAR(20),
	major VARCHAR(20)
);

CREATE TABLE accounts (
  user_id SERIAL PRIMARY KEY, 
  username VARCHAR (50) UNIQUE NOT NULL, 
  password VARCHAR (50) NOT NULL, 
  email VARCHAR (255) UNIQUE NOT NULL, 
  created_at TIMESTAMP NOT NULL, 
  last_login TIMESTAMP
);

INSERT INTO student(name, major)
VALUES ('Danny', '學生');

INSERT INTO student(name, major)
VALUES ('John', '學生');

Drop Table accounts;
Drop Table student;

CREATE TABLE IF NOT EXISTS student (
	student_id Serial Primary Key,
    name Varchar(20) Not Null,
    major Varchar(20)
);

