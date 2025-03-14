CREATE DATABASE knights;
USE knights;

CREATE TABLE favorite_colors (
  name VARCHAR(20) NOT NULL,
  color VARCHAR(10) NOT NULL
);

INSERT INTO favorite_colors (name, color)
VALUES
  ('Lancelot', 'blue'),
  ('Galahad', 'yellow');
