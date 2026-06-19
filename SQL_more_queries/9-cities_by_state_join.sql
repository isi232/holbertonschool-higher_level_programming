-- script that lists all cities contained in the database hbtn_0d_usa.
-- Each record displays: cities.id - cities.name - states.name
-- results sortes in ascending order by cities.id
-- used only one SELECT statement
SELECT cities.id, cities.name, states.name
FROM cities
LEFT JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;