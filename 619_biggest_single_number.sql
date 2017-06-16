# Write your MySQL query statement below
select max(n.num) as num
from number n
where n.num not in
(select num from number group by num having count(*) >= 2)
