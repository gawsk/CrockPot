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


-- Create recipe url table
CREATE TABLE recipe_url(
  id BIGINT NOT NULL AUTO_INCREMENT,
  url VARCHAR(1000) NOT NULL UNIQUE,
  PRIMARY KEY(id)
);


-- Create recipe table
CREATE TABLE recipe (
  id BIGINT NOT NULL AUTO_INCREMENT,
  name VARCHAR(200) NOT NULL,
  description VARCHAR(500),
  user_id BIGINT NOT NULL,
  url_id BIGINT NOT NULL,
  PRIMARY KEY(id),
  UNIQUE KEY(user_id, url_id),
  FOREIGN KEY(user_id) REFERENCES user(id),
  FOREIGN KEY(url_id) REFERENCES recipe_url(id)

);


-- CREATE recipe step table
CREATE TABLE recipe_step (
  id BIGINT NOT NULL AUTO_INCREMENT,
  recipe_id BIGINT NOT NULL,
  description TEXT NOT NULL,
  num BIGINT NOT NULL,
  PRIMARY KEY(id),
  FOREIGN KEY(recipe_id) REFERENCES recipe(id)
);


-- Create ingredient table
CREATE TABLE ingredient (
  id BIGINT NOT NULL AUTO_INCREMENT,
  name VARCHAR(130) NOT NULL,
  PRIMARY KEY(id)
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
  measurement_id BIGINT,
  recipe_id BIGINT NOT NULL,
  amount VARCHAR(25) NOT NULL DEFAULT 0,
  PRIMARY KEY(id),
  FOREIGN KEY(ingredient_id) REFERENCES ingredient(id),
  FOREIGN KEY(measurement_id) REFERENCES measurement(id),
  FOREIGN KEY(recipe_id) REFERENCES recipe(id)
);


-- Create allergies table with common allergies
CREATE TABLE allergy (
  id BIGINT NOT NULL AUTO_INCREMENT,
  name VARCHAR(100) NOT NULL,
  PRIMARY KEY(id)
);

INSERT INTO allergy VALUES(1, "milk");
INSERT INTO allergy VALUES(2, "peanuts");
INSERT INTO allergy VALUES(3, "eggs");
INSERT INTO allergy VALUES(4, "nuts");
INSERT INTO allergy VALUES(5, "soy");
INSERT INTO allergy VALUES(6, "wheat");
INSERT INTO allergy VALUES(7, "fish");
INSERT INTO allergy VALUES(8, "shellfish");
INSERT INTO allergy VALUES(9, "corn");
INSERT INTO allergy VALUES(10, "gelatin");
INSERT INTO allergy VALUES(11, "sesame");
INSERT INTO allergy VALUES(12, "sunflower");
INSERT INTO allergy VALUES(13, "poppy");


-- Create user allergies table to show relationship
CREATE TABLE user_allergy (
  allergy_id BIGINT NOT NULL,
  user_id BIGINT NOT NULL,
  FOREIGN KEY(allergy_id) REFERENCES allergy(id),
  FOREIGN KEY(user_id) REFERENCES user(id),
  UNIQUE(allergy_id, user_id)
);


COMMIT;
