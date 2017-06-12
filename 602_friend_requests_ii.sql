# Write your MySQL query statement below
select sub.id, count(*) as num
from
(
select requester_id as id from request_accepted
union all
(select accepter_id as id from request_accepted)
) sub
group by id order by count(*) desc limit 1
