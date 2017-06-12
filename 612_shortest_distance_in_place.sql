# Write your MySQL query statement below
select round(SQRT((a.x-b.x)*(a.x-b.x) + (a.y-b.y)*(a.y-b.y)),2) as shortest
from point_2d a
join point_2d b
where a.x <> b.x or a.y <> b.y
order by SQRT((a.x-b.x)*(a.x-b.x) + (a.y-b.y)*(a.y-b.y)) asc
limit 1
