/*
Enter your query here.
Query the list of CITY names from STATION that either do not start with vowels or do not end with vowels. Your result cannot contain duplicates.

Input Format

The STATION table is described as follows:

Station.jpg

where LAT_N is the northern latitude and LONG_W is the western longitude.


*/

SELECT DISTINCT(CITY)
FROM STATION
WHERE NOT SUBSTR(CITY,LENGTH(CITY),1) IN ('A','E','I','O','U') OR NOT SUBSTR(CITY,1,1) IN ('A','E','I','O','U')