-- loadint the categories dataset
LOAD DATA INFILE 'categories.csv'
INTO TABLE categories
FIELDS TERMINATED BY ','
LINETERMINATED BY '\n'
IGNORE 1 ROWS ;

-- loadint the business dataset
LOAD DATA INFILE 'business.csv'
INTO TABLE business
FIELDS TERMINATED BY ','
LINETERMINATED BY '\n'
IGNORE 1 ROWS ;

-- loadint the countries dataset
LOAD DATA INFILE 'countries.csv'
INTO TABLE countries
FIELDS TERMINATED BY ','
LINETERMINATED BY '\n'
IGNORE 1 ROWS ;
