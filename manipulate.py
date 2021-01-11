from script import business, countries, categories
import pandas as pd
from pandasql import PandaSQL

pdsql = PandaSQL()

#to find the oldest and the newsest business in the world
query = '''
SELECT min(year_founded)as min,
    max(year_founded)as max
FROM business
'''
print(pdsql(query))


#to find the information about business founded before the year 1000 and their catagories
query = '''
SELECT b.business, b.year_founded, c.category , co.country
FROM business b
INNER JOIN categories c ON c.category_id = b.category_id
INNER JOIN countries co ON co.country_id = b.country_id
WHERE year_founded < 1000
'''
print(pdsql(query))

# to find the number of top 10 catagories
query = '''
SELECT c.category , count(*) as count
FROM business b
INNER JOIN categories c ON c.category_id = b.category_id
GROUP BY c.category
ORDER BY count(*) DESC
LIMIT 10
'''
print(pdsql(query))


# counting the number of catagories per continent
query = '''
SELECT co.continent, c.category, count(*) as count
FROM business b
INNER JOIN categories c ON c.category_id = b.category_id
INNER JOIN countries co ON co.country_id = b.country_id
GROUP BY c.category, co.continent
ORDER BY co.continent
'''
print(pdsql(query))


