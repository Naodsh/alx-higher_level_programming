-- Calculate and display the top 3 cities by average temperature during July and August
SELECT city, ROUND(AVG(temperature), 4) AS avg_temp
FROM temperatures
WHERE MONTH(date) IN (7, 8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
