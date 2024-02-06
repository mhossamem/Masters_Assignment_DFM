SELECT station_name, YEAR(date_time) AS year, AVG(pm25_value) AS mean_pm25, AVG(vpm25_value) AS mean_vpm25
FROM pollution
WHERE TIME(date_time) = '08:00:00' AND YEAR(date_time) BETWEEN 2010 AND 2022
GROUP BY station_name, YEAR(date_time);