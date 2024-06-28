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

CREATE TABLE IF NOT EXISTS youbike (
	_id Serial Primary Key,
	sna VARCHAR (50),
	ar VARCHAR(100),
	mday timestamp,
	rent_bikes SMALLINT,
	return_bikes SMALLINT,
	lat REAL,
	lng REAL
);

Drop Table youbike;

INSERT INTO youbike(sna,sarea,ar,mday,updatetime,total,rent_bikes,return_bikes,lat,lng,act)
VALUES ('臺大明達館北側(員工宿舍)',
	    '臺大公館校區',
	    '明達館前側北空地',
	    '2024-06-24 13:58:29',
	    '2024-06-24 14:21:52',
	    18,
	    18,
	    0,
	    25.02112,
	    121.54469,
	    '1'	
	);