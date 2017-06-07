# Write your MySQL query statement below
select min(abs(a.x - b.x)) as shortest
from point a
join point b
on a.x <> b.x
