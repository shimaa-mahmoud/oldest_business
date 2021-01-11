CREATE TABLE categories (
  category_id INT PRIMARY KEY NOT NULL ,
  category VARCHAR(50)
);

CREATE TABLE countries (
  country_id PRIMARY KEY NOT NULL,
  Country VARCHAR(50),
  continent VARCHAR(20)
);

CREATE TABLE business (
  Business VARCHAR(64),
  year_founded INT,
  category_id INT,
  country_id INT
);

