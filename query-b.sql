SELECT station_name, AVG(pm25_value) AS mean_pm25, AVG(vpm25_value) AS mean_vpm25
FROM pollution
WHERE YEAR(date_time) = 2019 AND TIME(date_time) = '08:00:00'
GROUP BY station_name;