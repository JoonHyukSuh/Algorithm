SELECT datetime 
from (select * from animal_ins order by datetime)
where rownum = 1;