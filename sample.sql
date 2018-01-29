-- Create Database first

DROP DATABASE crockpot_db;
CREATE DATABASE crockpot_db;

-- Select the database
USE crockpot_db;


CREATE TABLE user (
  id BIGINT NOT NULL AUTO_INCREMENT,
  name VARCHAR(45) NULL,
  username VARCHAR(45) NOT NULL,
  password VARCHAR(45) NOT NULL,
  PRIMARY KEY (id)
);



COMMIT;
