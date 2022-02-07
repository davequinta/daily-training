/*
Enter your query here.
Query the list of CITY names from STATION which have vowels (i.e., a, e, i, o, and u) as both their first and last characters. Your result cannot contain duplicates.
*/
SELECT DISTINCT(CITY)
FROM STATION
WHERE SUBSTR(CITY,LENGTH(CITY),1) IN ('A','E','I','O','U') AND SUBSTR(CITY,1,1) IN ('A','E','I','O','U')