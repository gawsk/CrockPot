-- Create Database first

DROP DATABASE IF EXISTS crockpot_db;
CREATE DATABASE IF NOT EXISTS crockpot_db;

-- Select the database
USE crockpot_db;


-- Create role TABLE
CREATE TABLE role (
  id Integer NOT NULL AUTO_INCREMENT,
  name VARCHAR(50) NOT NULL UNIQUE,
  PRIMARY KEY(id)
);

INSERT INTO role VALUES(1, "Superadmin");
INSERT INTO role VALUES(2, "User");


-- Create user table
CREATE TABLE user (
  id BIGINT NOT NULL AUTO_INCREMENT,
  email VARCHAR(320) NOT NULL UNIQUE,
  name VARCHAR(45) NULL,
  username VARCHAR(45) NOT NULL UNIQUE,
  password VARCHAR(150) NOT NULL,
  role_id Integer DEFAULT 2,
  PRIMARY KEY (id),
  FOREIGN KEY(role_id) REFERENCES role(id)
);


-- Create recipe table
CREATE TABLE recipe (
  id BIGINT NOT NULL AUTO_INCREMENT,
  name VARCHAR(200) NOT NULL,
  description VARCHAR(500),
  user_id BIGINT NOT NULL,
  PRIMARY KEY(id),
  FOREIGN KEY(user_id) REFERENCES user(id)
);


-- CREATE recipe steps table
CREATE TABLE recipe_steps (
  id BIGINT NOT NULL AUTO_INCREMENT,
  recipe_id BIGINT NOT NULL,
  description TEXT NOT NULL,
  PRIMARY KEY(id),
  FOREIGN KEY(recipe_id) REFERENCES recipe(id)
);


-- Create ingredient table
CREATE TABLE ingredient (
  id BIGINT NOT NULL AUTO_INCREMENT,
  name VARCHAR(130) NOT NULL,
  recipe_id BIGINT NOT NULL,
  PRIMARY KEY(id),
  FOREIGN KEY(recipe_id) REFERENCES recipe(id)
);


-- Create measurement table (
CREATE TABLE measurement (
  id BIGINT NOT NULL AUTO_INCREMENT,
  name varchar(50) NOT NULL,
  PRIMARY KEY(id)
);


-- Create quantity table
CREATE TABLE quantity (
  id BIGINT NOT NULL AUTO_INCREMENT,
  ingredient_id BIGINT NOT NULL,
  measurement_id BIGINT NOT NULL,
  amount int NOT NULL DEFAULT 0,
  PRIMARY KEY(id),
  FOREIGN KEY(ingredient_id) REFERENCES ingredient(id),
  FOREIGN KEY(measurement_id) REFERENCES measurement(id)
);



COMMIT;
