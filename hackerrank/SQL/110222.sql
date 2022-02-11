/*
Enter your query here.
Query the list of CITY names from STATION that do not start with vowels and do not end with vowels. Your result cannot contain duplicates.
*/

SELECT DISTINCT(CITY)
FROM STATION
WHERE NOT SUBSTR(CITY,LENGTH(CITY),1) IN ('A','E','I','O','U') AND NOT SUBSTR(CITY,1,1) IN ('A','E','I','O','U')