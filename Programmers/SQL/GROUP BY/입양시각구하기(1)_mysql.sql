select hour(datetime) as hour, count(datetime) as count
from animal_outs
group by hour
having hour >= 9 and hour <20
order by hour asc