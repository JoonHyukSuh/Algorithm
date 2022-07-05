select if (G.grade < 8, 'NULL', S.name), G.grade, S.marks
from students S
inner join grades G
on S.marks between G.Min_Mark and G.Max_Mark
order by G.grade desc, S.name asc

