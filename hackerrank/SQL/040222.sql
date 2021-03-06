/*
Enter your query here.
Query the list of CITY names starting with vowels (i.e., a, e, i, o, or u) from STATION. Your result cannot contain duplicates.

Input Format
*/
SELECT DISTINCT(CITY)
FROM STATION
WHERE SUBSTR(CITY,1,1) IN ('A','E','I','O','U') 