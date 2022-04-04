select city, length(city)
from (select * 
     from station 
     order by length(city) asc, city asc)
where rownum = 1;
select city, length(city)
from (select * 
     from station 
     order by length(city) desc, city asc)
where rownum = 1; 
