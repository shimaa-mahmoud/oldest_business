-- to find the oldest and the newsest business in the world 

SELECT min(year_founded)as min,
    max(year_founded)as max
FROM business


-- to find the information about business founded before the year 1000 and their catagories 
SELECT b.business, b.year_founded, c.catagory , co.country
FROM business b
INNER JOIN categories c ON c.category_id = b.category_id
INNER JOIN countries co ON co.country_id = b.country_id
WHERE year_founded < 1000

-- to find the top 10 catagories 

SELECT c.category , count(*) as count
FROM business b
INNER JOIN categories c ON c.category_id = b.category_id
GROUP BY c.category
ORDER BY count(*) DESC
LIMIT 10

-- counting the number of catagories per continent 

SELECT co.continent, c.category, count(*) as count
FROM business b
INNER JOIN categories c ON c.category_id = b.category_id
INNER JOIN countries co ON co.country_id = b.country_id
GROUP BY c.category, co.continent
ORDER BY co.continent
