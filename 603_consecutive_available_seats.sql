# Write your MySQL query statement below
select distinct a.seat_id as seat_id
from cinema a
join cinema b
on a.seat_id + 1 = b.seat_id or a.seat_id = b.seat_id + 1
where a.free = 1 and b.free = 1 
order by a.seat_id
