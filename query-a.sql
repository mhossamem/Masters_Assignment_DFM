SELECT date_time, station_name, MAX(nox_value) AS highest_nox
FROM pollution
WHERE YEAR(date_time) = 2022
GROUP BY date_time, station_name;