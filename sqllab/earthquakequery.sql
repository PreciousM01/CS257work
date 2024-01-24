-- Display the id and the earthquake depth columns for earthquakes whose depths are greater than 100
SELECT id, quakedepth FROM earthquakes WHERE quakedepth>10;

-- Display the id, status and date of earthquakes with status marked 'reviewed'. Order by id in acending order.
SELECT id, quakestatus, quakedate FROM earthquakes WHERE quakestatus ='reviewed' 
ORDER BY id ASC;

--Displaying all colums for eathquakes than happened between 2023-01-01 and 2023-01-15
SELECT * FROM earthquakes WHERE quakedate BETWEEN '2023-01-01' AND '2023-01-15';
