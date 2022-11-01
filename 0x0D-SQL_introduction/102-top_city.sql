-- script that displays the top 3 of cities temperature during July and August ordered by temperature (descending)
SELECT city,avg_temp FROM (SELECT city,
 AVG(value) AS avg_temp
 FROM temperatures
 WHERE month = 7 OR month = 8
 GROUP BY city
 ORDER BY AVG(value) DESC) results LIMIT 3;
